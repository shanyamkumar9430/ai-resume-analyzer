
from flask import Flask, render_template, request
import fitz
from analyzer import analyze_resume

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = None

    if request.method == "POST":

        resume = request.files.get("resume")
        job_description = request.form.get("job_description", "")

        if not resume or not resume.filename.lower().endswith(".pdf"):
            error = "Please upload a valid PDF resume."

        elif not job_description.strip():
            error = "Please enter a job description."

        else:
            try:
                pdf = fitz.open(stream=resume.read(), filetype="pdf")

                resume_text = "\n".join(
                    page.get_text() for page in pdf
                )

                pdf.close()

                if not resume_text.strip():
                    error = "No readable text found in this PDF."

                else:
                    result = analyze_resume(
                        resume_text,
                        job_description
                    )

            except Exception:
                error = "Unable to read this PDF. Please try another file."

    return render_template(
        "index.html",
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
