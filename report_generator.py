from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

import datetime

def generate_report(company, industry, revenue, employees, score, industry_avg, difference, recommendations, roadmap):

    filename = f"{company}_Scorvanta_Report.pdf"
    doc = SimpleDocTemplate(filename)

    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph("<b>Scorvanta AI - Executive Report</b>", styles["Title"]))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph(f"Company: {company}", styles["Normal"]))
    elements.append(Paragraph(f"Industry: {industry}", styles["Normal"]))
    elements.append(Paragraph(f"Revenue: ₹{revenue} Cr", styles["Normal"]))
    elements.append(Paragraph(f"Employees: {employees}", styles["Normal"]))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph("<b>CEO Executive Summary</b>", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    summary_text = f"""
    Your AI readiness score is {score}/100.
    Industry benchmark is {industry_avg}.
    Competitive gap: {difference}.
    AI maturity directly impacts operational efficiency and long-term revenue scaling.
    Strategic AI investment recommended to improve competitiveness.
    """

    elements.append(Paragraph(summary_text, styles["Normal"]))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph("<b>Strategic Recommendations</b>", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    rec_list = [ListItem(Paragraph(r, styles["Normal"])) for r in recommendations]
    elements.append(ListFlowable(rec_list, bulletType='bullet'))

    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph("<b>AI Adoption Roadmap</b>", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    roadmap_list = [ListItem(Paragraph(r, styles["Normal"])) for r in roadmap]
    elements.append(ListFlowable(roadmap_list, bulletType='bullet'))

    doc.build(elements)

    return filename