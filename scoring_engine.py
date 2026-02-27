# scoring_engine.py

def calculate_score(digital, automation, ai_invest, data_maturity, rnd):
    score = (
        digital * 0.20 +
        automation * 0.20 +
        ai_invest * 0.20 +
        data_maturity * 0.20 +
        rnd * 0.20
    ) * 5

    return round(score, 2)


def risk_level(score):
    if score < 40:
        return "High Risk"
    elif score < 70:
        return "Moderate Risk"
    else:
        return "Competitive"


def compare_with_benchmark(score, industry, industry_benchmarks):
    industry_avg = industry_benchmarks[industry]
    difference = round(score - industry_avg, 2)

    if score > industry_avg:
        status = "Above Industry Average"
    elif score < industry_avg:
        status = "Below Industry Average"
    else:
        status = "At Industry Average"

    return industry_avg, status, difference


def competitive_index(score, industry_avg):
    if industry_avg == 0:
        return 0
    return round((score / industry_avg) * 100, 2)


def roi_projection(score, revenue):
    if score < 40:
        growth_factor = 0.05
    elif score < 60:
        growth_factor = 0.10
    elif score < 80:
        growth_factor = 0.18
    else:
        growth_factor = 0.25

    projected_revenue = revenue * (1 + growth_factor)
    uplift = projected_revenue - revenue

    return round(projected_revenue, 2), round(uplift, 2)


def three_year_projection(score, revenue):
    if score < 50:
        rate = 0.08
    elif score < 75:
        rate = 0.15
    else:
        rate = 0.22

    year1 = revenue * (1 + rate)
    year2 = year1 * (1 + rate)
    year3 = year2 * (1 + rate)

    return round(year1,2), round(year2,2), round(year3,2)


def ai_roadmap(score):
    if score < 40:
        return [
            "Digitize core operations",
            "Implement ERP & CRM systems",
            "Basic data collection framework"
        ]
    elif score < 70:
        return [
            "Automate repetitive workflows",
            "Deploy predictive analytics",
            "Build internal AI taskforce"
        ]
    else:
        return [
            "Deploy AI-driven decision systems",
            "Invest in proprietary AI models",
            "Scale AI across departments"
        ]