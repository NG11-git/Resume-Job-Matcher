SKILLS = [
    "python", "sql", "machine learning", "deep learning", 
    "data analysis", "data visualization", "nlp",
    "cv", "scikt-learn", "tensorflow", "pytorch", "bert", "streamlit", "fastapi",
    "aws", "azure", "gcp", "docker", "kubernetes", "git", "communication", "teamwork", "problem-solving", "critical thinking",
    "opencv", "keras", "xgboost", "lightgbm", "catboost", "hadoop", "spark", "airflow",
    "tableau", "power bi", "excel", "bigquery", "redshift", "snowflake", "linux", "bash", "rest api", "graphql", "ci/cd",
    "agile", "scrum", "kanban", "project management", "time management", "leadership", "mentoring"
]

def extract_skills(text):
    text = text.lower()
    return [skill for skill in SKILLS if skill in text]


def skill_gap(resume_skills, jd_skills):
    missing = jd_skills - resume_skills
    matched =  resume_skills & jd_skills
    return matched, missing