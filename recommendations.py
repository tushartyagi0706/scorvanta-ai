# recommendations.py

def generate_recommendations(score):
    if score < 40:
        return [
            "Invest in digital infrastructure immediately.",
            "Start process automation in operations.",
            "Allocate 3-5% of revenue toward AI initiatives."
        ]
    elif score < 70:
        return [
            "Expand AI analytics across departments.",
            "Upskill workforce in AI tools.",
            "Increase automation in supply chain and operations."
        ]
    else:
        return [
            "Invest in AI-driven innovation.",
            "Build internal AI research capabilities.",
            "Explore AI-based new revenue streams."
        ]