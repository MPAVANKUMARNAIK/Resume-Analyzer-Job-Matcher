from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume_job(resume_text, job_desc):
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume_text, job_desc])
    score = cosine_similarity(vectors)[0][1] * 100

    # Boost score if keywords match strongly
    common_words = set(resume_text.lower().split()) & set(job_desc.lower().split())
    bonus = min(len(common_words) * 0.1, 10)

    return round(score + bonus, 2)