import streamlit as st
import pandas as pd
import plotly.express as px

from utils.parser import extract_text_from_pdf, extract_skills
from utils.matcher import match_resume_job
from utils.ai_suggestions import get_suggestions
from utils.db import init_db, save_score
from utils.report import create_pdf
from utils.skill_gap import skill_gap
from utils.chatbot import chat_with_ai

st.set_page_config(page_title="AI Resume Analyzer Elite", layout="wide")

# -----------------------------
#  JOB RECOMMENDER FUNCTION
# -----------------------------
def recommend_jobs(skills):
    skills = [s.lower() for s in skills]

    roles = {
        "Software Developer": ["c++", "java", "python", "sql"],
        "Backend Developer": ["python", "java", "node", "sql"],
        "AI Engineer": ["python", "ai", "machine learning"],
        "Frontend Developer": ["html", "css", "javascript"]
    }

    results = []
    for role, req in roles.items():
        match = len(set(skills) & set(req))
        score = int((match / len(req)) * 100)
        results.append((role, score))

    return sorted(results, key=lambda x: x[1], reverse=True)

# -----------------------------
# UI
# -----------------------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] { 
    background: #EEF2F7; 
    color: #111827;
}

.block-container {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    max-width: 1400px;
    margin: auto;
    color: #111827;
}

h1 {
    background: linear-gradient(90deg,#2563EB,#1D4ED8);
    color: #ffffff !important;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}

.job-card {
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
    font-size: 16px;
    color: #111827;
}

.best {
    background-color: #D1FAE5;
    color: #064E3B;
    font-weight: bold;
}

.other {
    background-color: #E5E7EB;
    color: #111827;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.header("🚀 Resume Tips")
    st.info("✔ Use action verbs")
    st.info("✔ Add measurable achievements")
    st.info("✔ Include latest tools")
    st.info("✔ Customize per job")

# -----------------------------
# INIT
# -----------------------------
init_db()

st.markdown("<h1>AI Resume Analyzer & Job Matcher</h1>", unsafe_allow_html=True)

job_desc = st.text_area("📌 Paste Job Description")
uploaded_files = st.file_uploader("📂 Upload Resume(s)", type=["pdf"], accept_multiple_files=True)

st.markdown("---")

#  FULL WIDTH (NO RIGHT COLUMN NOW)
left = st.container()

# -----------------------------
# MAIN CONTENT
# -----------------------------
with left:

    if uploaded_files:
        results = []

        for f in uploaded_files:
            text = extract_text_from_pdf(f)
            skills = extract_skills(text)

            score = match_resume_job(text, job_desc) if job_desc else 0
            save_score("guest", score)

            suggestions = get_suggestions(text)

            results.append({
                "name": f.name,
                "skills": skills,
                "score": score,
                "text": text,
                "suggestions": suggestions
            })

        for i, r in enumerate(results):
            st.markdown(f"## 📄 {r['name']}")

            col1, col2, col3 = st.columns([2,1,1])

            with col1:
                st.markdown("### 🧠 Skills")
                st.markdown(" ".join([f"`{s}`" for s in r["skills"]]))

                st.markdown("### 🎯 Best Job Roles for You")

                job_matches = recommend_jobs(r["skills"])

                best_role, best_score = job_matches[0]

                st.markdown(f"""
                <div class="job-card best">
                🎯 Best Role: {best_role} ({best_score}%)
                </div>
                """, unsafe_allow_html=True)

                for role, score_val in job_matches[1:4]:
                    st.markdown(f"""
                    <div class="job-card other">
                    {role}: {score_val}%
                    </div>
                    """, unsafe_allow_html=True)

            with col2:
                st.metric("Score", f"{r['score']}%")
                st.progress(int(r["score"]))

            with col3:
                st.info(f"Skills: {len(r['skills'])}")

            if r["score"] > 75:
                st.success("🔥 Highly Suitable")
            elif r["score"] > 50:
                st.warning("Moderate Fit")
            else:
                st.error("❌ Needs Improvement")

            if job_desc:
                matched, missing = skill_gap(r["skills"], job_desc)

                st.markdown("### ❌ Missing Skills")
                if missing:
                    st.error(", ".join(missing))

                    st.markdown("### 🎯 How to Improve")
                    for skill in missing[:5]:
                        st.info(f"👉 Learn {skill} + build project")

                else:
                    st.success("No missing skills 🎉")

            st.markdown("###  AI Suggestions")
            st.info(r["suggestions"])

            fig_pie = px.pie(
                names=["Match", "Gap"],
                values=[r["score"], 100-r["score"]],
                title="Match vs Gap"
            )
            st.plotly_chart(fig_pie, use_container_width=True)

            with st.expander("📄 Resume Preview"):
                st.text(r["text"][:1200])

            st.markdown("---")

        st.markdown("## 🏆 Ranking")
        ranked = sorted(results, key=lambda x: x["score"], reverse=True)

        for i, r in enumerate(ranked, 1):
            st.write(f"{i}. {r['name']} - {r['score']}%")

        st.markdown("## 📊 Dashboard")

        names = [r["name"] for r in results]
        scores = [r["score"] for r in results]

        fig_bar = px.bar(
            x=names,
            y=scores,
            color=scores,
            text=scores,
            color_continuous_scale="Blues",
            title="Resume Match Comparison"
        )

        st.plotly_chart(fig_bar, use_container_width=True)