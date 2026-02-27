import streamlit as st
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet
import os

# =============================
# PAGE CONFIG
# =============================

st.set_page_config(
    page_title="Scorvanta AI",
    page_icon="assets/scorvanta_logo.png",
    layout="wide"
)

# =============================
# LOGO
# =============================

if os.path.exists("assets/scorvanta_logo.png"):
    st.image("assets/scorvanta_logo.png", width=180)

st.title("Scorvanta AI – Competitiveness Analyzer")

st.success("🟢 Beta Mode Active (All Features Free)")

# =============================
# COMPANY INPUT
# =============================

company_name = st.text_input("Company Name")
industry = st.selectbox("Industry", ["Manufacturing", "IT", "Finance", "Healthcare", "Retail"])

# =============================
# REVENUE SECTION (MULTI UNIT)
# =============================

st.subheader("Annual Revenue")

col1, col2 = st.columns(2)

with col1:
    revenue_value = st.number_input("Enter Revenue Value", min_value=0.0, value=100.0)

with col2:
    revenue_unit = st.selectbox("Select Revenue Unit", 
        ["Thousand", "Lakh", "Crore", "Million", "Billion"])

# Convert everything to Crores internally

def convert_to_crore(value, unit):
    if unit == "Thousand":
        return value / 100000
    elif unit == "Lakh":
        return value / 100
    elif unit == "Crore":
        return value
    elif unit == "Million":
        return value * 0.1
    elif unit == "Billion":
        return value * 100
    return value

revenue_crore = convert_to_crore(revenue_value, revenue_unit)

employees = st.slider("Number of Employees", 1, 10000, 100)

# =============================
# AI CAPABILITY SLIDERS
# =============================

st.subheader("Rate Your AI Capability (0-20 Scale)")

digital = st.slider("Digital Infrastructure", 0, 20, 10)
automation = st.slider("Automation Level", 0, 20, 10)
ai_invest = st.slider("AI Investment Level", 0, 20, 10)
data_maturity = st.slider("Data Maturity", 0, 20, 10)
rnd = st.slider("R&D Intensity", 0, 20, 10)

# =============================
# SCORING ENGINE
# =============================

score = round(((digital + automation + ai_invest + data_maturity + rnd) / 100) * 100, 2)

st.subheader("AI Readiness Score")
st.metric("Score", f"{score}/100")

if score < 40:
    risk = "High Risk"
elif score < 70:
    risk = "Moderate Risk"
else:
    risk = "Competitive"

st.warning(risk)

# =============================
# ROI PROJECTION
# =============================

uplift_percent = score / 10  # up to 10% uplift

year1 = revenue_crore
year2 = revenue_crore * (1 + uplift_percent / 100)
year3 = year2 * (1 + uplift_percent / 100)

st.subheader("Projected ROI Impact")

st.write(f"Current Revenue: ₹ {round(year1,2)} Cr")
st.write(f"Projected Revenue (Next 3 Years): ₹ {round(year3,2)} Cr")
st.success(f"Estimated Revenue Uplift: ₹ {round(year3 - year1,2)} Cr")

# =============================
# GRAPH
# =============================

st.subheader("3-Year AI Revenue Projection")

years = ["Year 1", "Year 2", "Year 3"]
revenues = [year1, year2, year3]

fig, ax = plt.subplots()
ax.plot(years, revenues, marker='o')
ax.set_ylabel("Revenue (₹ Crores)")
ax.set_title("3-Year AI Revenue Projection")

st.pyplot(fig)

# =============================
# EXECUTIVE INSIGHT
# =============================

st.subheader("Executive Insight")

if score < 50:
    insight = "AI maturity below industry benchmark. Immediate structural upgrades recommended."
else:
    insight = "AI maturity strong. Focus on scaling automation & predictive intelligence."

st.info(insight)

# =============================
# ROADMAP
# =============================

st.subheader("Strategic AI Roadmap")

st.write("• Phase 1 (0-6 Months): Build AI data foundation & governance.")
st.write("• Phase 2 (6-18 Months): Deploy automation across key operations.")
st.write("• Phase 3 (18-36 Months): Scale predictive AI & decision intelligence.")

# =============================
# RECOMMENDATIONS
# =============================

st.subheader("AI Recommendations")

st.write("• Expand AI analytics across departments.")
st.write("• Upskill workforce in AI tools.")
st.write("• Increase automation in supply chain and operations.")

# =============================
# PDF GENERATION
# =============================

if st.button("Download Executive PDF Report"):

    doc = SimpleDocTemplate("Scorvanta_Report.pdf")
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph("Scorvanta AI - Executive Report", styles['Title']))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph(f"Company: {company_name}", styles['Normal']))
    elements.append(Paragraph(f"Industry: {industry}", styles['Normal']))
    elements.append(Paragraph(f"Revenue: ₹ {round(revenue_crore,2)} Cr", styles['Normal']))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph("CEO Executive Summary", styles['Heading2']))
    elements.append(Paragraph(f"AI Readiness Score: {score}/100", styles['Normal']))
    elements.append(Paragraph(insight, styles['Normal']))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph("Strategic Recommendations", styles['Heading2']))

    bullet_points = [
        "Expand AI analytics across departments.",
        "Upskill workforce in AI tools.",
        "Increase automation in supply chain."
    ]

    elements.append(ListFlowable(
        [ListItem(Paragraph(point, styles['Normal'])) for point in bullet_points]
    ))

    doc.build(elements)

    with open("Scorvanta_Report.pdf", "rb") as f:
        st.download_button("Click Here to Download", f, file_name="Scorvanta_Report.pdf")
