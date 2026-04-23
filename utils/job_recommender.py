def recommend_jobs(skills):
    
    skills = [s.lower() for s in skills]

    roles = {
        "Frontend Developer": ["html", "css", "javascript", "react"],
        "Backend Developer": ["python", "java", "node", "sql"],
        "Full Stack Developer": ["html", "css", "javascript", "react", "node", "sql"],
        "Data Scientist": ["python", "machine learning", "ai", "pandas", "numpy"],
        "AI Engineer": ["python", "ai", "deep learning", "ml"],
        "Software Developer": ["c++", "java", "python", "sql"]
    }

    results = []

    for role, role_skills in roles.items():
        match = len(set(skills) & set(role_skills))
        score = int((match / len(role_skills)) * 100)

        results.append((role, score))

    # Sort best first
    results.sort(key=lambda x: x[1], reverse=True)

    return results