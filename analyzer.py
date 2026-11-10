
import re

SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "machine learning",
    "deep learning",
    "flask",
    "django",
    "html",
    "css",
    "javascript",
    "react",
    "pandas",
    "numpy",
    "scikit-learn",
    "data analysis",
    "nlp",
    "tensorflow",
    "pytorch",
    "git",
    "rest api",
    "mysql",
    "mongodb"
]

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9+#.\s]", " ", text)
    return text



def extract_skills(text):
    text = clean_text(text)

    found = []

    for skill in SKILLS:
        pattern = r"(?<![a-z0-9+#])" + re.escape(skill) + r"(?![a-z0-9+#])"

        if re.search(pattern, text):
            found.append(skill)

    return found

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match(resume_text, job_description):

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([
        resume_text,
        job_description
    ])

    score = cosine_similarity(
        vectors[0],
        vectors[1]
    )[0][0]

    return round(score * 100, 2)

def analyze_resume(resume_text, job_description):

    resume_skills = extract_skills(resume_text)

    required_skills = extract_skills(job_description)

    matched_skills = [
        skill for skill in required_skills
        if skill in resume_skills
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill not in resume_skills
    ]

    score = calculate_match(
        resume_text,
        job_description
    )

    return {
        "match_score": score,
        "resume_skills": resume_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }
