import streamlit as st
from src.skill_extractor import extract_skills, skill_gap
from src.embedding import get_embedding, extract_text_from_pdf
from src.preprocessing import clean_text
from src.scorer import compute_similarity

st.title("📄 :blue[_AI Resume Job Matcher_]")

resume_pdf = st.sidebar.file_uploader(
    "Upload Resume (PDF format)", type=["pdf"], accept_multiple_files=False
)

if resume_pdf is not None:
    st.sidebar.success("Resume uploaded successfully!")
else:
    st.sidebar.info("Please upload a resume in PDF format to proceed.")


jd_text = st.sidebar.text_area(
    "Enter Job Description: ", placeholder="Paste the job description here..."
    )


submit_button = st.sidebar.button("submit")

st.divider()

if submit_button:
    if resume_pdf and jd_text:
        resume_text = extract_text_from_pdf(resume_pdf)

        resume_clean_text = clean_text(resume_text)
        jd_clean_text = clean_text(jd_text)

        res_emb = get_embedding(resume_clean_text)
        jd_emb = get_embedding(jd_clean_text)

        score = compute_similarity(res_emb, jd_emb)
        score_percentage = round(score * 100, 2)

        resume_skills = extract_skills(resume_clean_text)
        jd_skills = extract_skills(jd_clean_text)

        matched, missing = skill_gap(set(resume_skills), set(jd_skills))

        if score_percentage > 75:
            st.success(f"Excellent Match! Your resume is {score_percentage}% aligned with the job description.")
        elif score_percentage > 60:
            st.warning(f"Good Match! Your resume is {score_percentage}% aligned with the job description. Consider improving it further.")
        else:
            st.error(f"Poor Match! Your resume is only {score_percentage}% aligned with the job description. Consider revising it to better fit this job role.")
        


        

        st.subheader("✅ Matched Skills")
        st.write(list(matched))

        st.subheader("❌ Missing Skills")
        st.write(list(missing))
