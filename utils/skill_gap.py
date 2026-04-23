import re

#  Define only meaningful technical skills
TECH_SKILLS = {
    "python", "java", "c++", "c", "sql", "html", "css", "javascript",
    "react", "node", "django", "flask", "mongodb", "mysql",
    "machine learning", "ai", "data science", "deep learning",
    "pandas", "numpy", "git", "github", "docker", "kubernetes"
}

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9+# ]', ' ', text)
    return text

def extract_skills_from_jd(job_desc):
    job_desc = clean_text(job_desc)

    found_skills = set()
    for skill in TECH_SKILLS:
        if skill in job_desc:
            found_skills.add(skill)

    return found_skills

def skill_gap(resume_skills, job_desc):
    jd_skills = extract_skills_from_jd(job_desc)
    resume_set = set([s.lower() for s in resume_skills])

    matched = resume_set & jd_skills
    missing = jd_skills - resume_set

    return list(matched), list(missing)