from pathlib import Path
from embedding import get_embedding
from preprocessing import clean_text
from scorer import compute_similarity
from skill_extractor import extract_skills, skill_gap

# Load sample files
resume_text = Path("resume-job-matcher/data/sample_resumes/resume_data_analyst_1.txt").read_text()
jd_text = Path("resume-job-matcher/data/samples_jds/jd_data_analyst.txt").read_text()

# Preprocess texts
resume_text = clean_text(resume_text)
jd_text = clean_text(jd_text)

# Embeddings
resume_emb = get_embedding(resume_text)
jd_emb = get_embedding(jd_text)

# Similarity checking
score = compute_similarity(resume_emb, jd_emb)
print(f"Similarity Score: {score:.4f}")


# Skill gap analysis

resume_skills = extract_skills(resume_text)
jd_skills = extract_skills(jd_text)

matched, missing = skill_gap(set(resume_skills), set(jd_skills))
print(f"Matched Skills: {matched}")
print(f"Missing Skills: {missing}")