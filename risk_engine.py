def assess_risk(country):
    high_risk = ["China", "Russia", "Iran", "North Korea"]
    medium_risk = ["Germany", "France"]

    if country in high_risk:
        return "high"
    elif country in medium_risk:
        return "medium"
    else:
        return "low"