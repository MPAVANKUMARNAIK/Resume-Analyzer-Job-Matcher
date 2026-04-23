# 🚀 AI Resume Analyzer & Job Matcher

A smart Python-based tool that analyzes resumes and matches them with job descriptions using NLP techniques.
This project helps fresh graduates improve their resumes and increase their chances of getting shortlisted.

---

## 📌 Problem Statement

Fresh graduates often struggle to tailor their resumes according to job roles.
This project solves that by analyzing resumes and comparing them with job descriptions.

---

## 🎯 Objectives

* Extract key information from resumes
* Compare skills with job requirements
* Generate a match score
* Suggest missing skills

---

## 🧠 Key Features

✔ Upload Resume (PDF/Text)
✔ NLP-based Keyword Extraction (NLTK / spaCy)
✔ Skill Matching with Job Description
✔ Resume Score (e.g., 75% match)
✔ Missing Skills Suggestions
✔ Best Job Role Recommendations

---

## 🖼️ Project Screenshots

### 🔹 Step 1: Upload Resume & Job Description

![Upload Screen](https://github.com/MPAVANKUMARNAIK/Resume-Analyzer-Job-Matcher/blob/f8e3287967831d955c2eec2dff0e7ffa30644db2/images/Screenshot%202026-04-23%20151032.png?raw=true)

👉 Users can paste the job description and upload their resume easily through a clean interface.

---

### 🔹 Step 2: Resume Analysis & Skill Extraction

![Analysis](https://github.com/MPAVANKUMARNAIK/Resume-Analyzer-Job-Matcher/blob/183c586eabe533e485c2fad989358828a6e1c0ae/images/Screenshot%202026-04-23%20151110.png?raw=true)

👉 The system extracts skills like Python, Java, SQL, etc., using NLP techniques and prepares them for comparison.

---

### 🔹 Step 3: Match Score & Job Role Suggestions

![Results](https://github.com/MPAVANKUMARNAIK/Resume-Analyzer-Job-Matcher/blob/183c586eabe533e485c2fad989358828a6e1c0ae/images/Screenshot%202026-04-23%20151307.png?raw=true)

👉 The tool generates:

* Match Score (e.g., 11.04%)
* Best Job Role Recommendation
* Skill match breakdown

---

## ⚙️ Tech Stack

* Python 🐍
* Streamlit 🎨
* NLP (NLTK / spaCy)
* PDF Processing (PyPDF2 / pdfminer)

---

## 🏗️ Project Structure

```
Resume-Analyzer/
│
├── app.py
├── utils.py
├── requirements.txt
├── Project_images/
│   ├── Screenshot 2026-04-23 151032.png
│   ├── Screenshot 2026-04-23 151110.png
└── README.md
```

---

## 🚀 Installation & Setup

```bash
# Clone repository
git clone https://github.com/your-username/Resume-Analyzer.git

# Navigate to project
cd Resume-Analyzer

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
```

---

## 💡 How It Works

1. Upload your resume (PDF/Text)
2. Paste job description
3. System extracts skills using NLP
4. Matches resume with job requirements
5. Generates:

   * Match Score
   * Missing Skills
   * Best Job Roles

---

## 📊 Example Output

* Match Score: **75%**
* Missing Skills: **React, AWS**
* Suggested Role: **Software Developer**

---

## 🔮 Future Enhancements

* AI-based resume rewriting
* Multi-language support
* LinkedIn profile integration
* Advanced ML models for better accuracy

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and improve the project.

---

## 📜 License

This project is open-source under the MIT License.

---

## 👨‍💻 Author

**Pavan Kumar Naik**
