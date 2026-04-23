import spacy
from pdfminer.high_level import extract_text

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file):
    return extract_text(file)

def extract_skills(text):
    doc = nlp(text)
    keywords = ["python","java","sql","react","node","machine","learning","ai","ml","c++","html","css"]
    skills = set()
    for token in doc:
        t = token.text.lower()
        if t in keywords:
            skills.add(t)
    return list(skills)