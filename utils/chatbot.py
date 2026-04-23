import google.generativeai as genai

# Configure API
genai.configure(api_key="AIzaSyAbm_R3EEqf-mLHd2pWSulK1M78jAzuL9Y")

# USE SAFE MODEL (WORKS EVERYWHERE)
model = genai.GenerativeModel("models/text-bison-001")

def chat_with_ai(messages, resume_text):
    try:
        prompt = f"""
You are a professional career assistant.

Resume:
{resume_text[:2000]}

Conversation:
"""

        for m in messages:
            role = "User" if m["role"] == "user" else "Assistant"
            prompt += f"{role}: {m['content']}\n"

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return "⚠ AI temporarily unavailable. Please try again."