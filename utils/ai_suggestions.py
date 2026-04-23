import os

def get_suggestions(text):
    try:
        import google.generativeai as genai

        
        api_key = "API_KEY"

        # Configure Gemini
        genai.configure(api_key=api_key)

        # Load model
        model = genai.GenerativeModel("gemini-pro")

        # Generate response
        resp = model.generate_content(
            f"Improve this resume with bullet points and ATS tips:\n{text[:6000]}"
        )

        return resp.text

    except Exception as e:
        print("Error:", e)

    return "Add quantified achievements, tailor skills to the job, and include strong action verbs."
