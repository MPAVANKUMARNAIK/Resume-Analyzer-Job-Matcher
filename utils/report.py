from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(name, score, suggestions):
    path = f"{name}_report.pdf"
    doc = SimpleDocTemplate(path)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("AI Resume Analysis Report", styles['Title']))
    content.append(Spacer(1,20))

    content.append(Paragraph(f"<b>Resume:</b> {name}", styles['Normal']))
    content.append(Spacer(1,10))

    content.append(Paragraph(f"<b>Match Score:</b> {score}%", styles['Normal']))
    content.append(Spacer(1,20))

    content.append(Paragraph("<b>AI Suggestions:</b>", styles['Heading2']))
    content.append(Spacer(1,10))

    for line in suggestions.split("\n"):
        content.append(Paragraph(f"- {line}", styles['Normal']))

    doc.build(content)
    return path