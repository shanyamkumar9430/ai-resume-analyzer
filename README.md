
# CareerMatch AI – Resume Analyzer

An AI-powered Resume Analyzer built using Python and Flask. It helps job seekers compare their resumes with job descriptions and identify relevant and missing skills.

## Features

- Upload resumes in PDF format.
- Extract text from PDF resumes.
- Identify technical skills automatically.
- Compare resumes with job descriptions.
- Calculate a text similarity score.
- Display matched and missing skills.
- Simple and responsive web interface.

## Technologies Used

- Python
- Flask
- Natural Language Processing (NLP)
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- PyMuPDF
- HTML and CSS

## Project Structure

```text
ai-resume-analyzer/
│
├── analyzer.py
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── templates/
    └── index.html
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/shanyamkumar9430/ai-resume-analyzer.git
```

2. Open the project folder:

```bash
cd ai-resume-analyzer
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python3 app.py
```

5. Open your browser:

```text
http://127.0.0.1:5000
```

## How It Works

1. Upload a PDF resume.
2. Paste the target job description.
3. The application extracts resume text.
4. It identifies skills from the resume and job description.
5. TF-IDF and cosine similarity calculate a text similarity score.
6. The results display matched and missing skills.

## Important Note

This project is developed for educational purposes. The match percentage represents text similarity and should not be treated as a guaranteed measure of a candidate's suitability for a job.

## Author

Shanyam Kumar

GitHub: https://github.com/shanyamkumar9430
