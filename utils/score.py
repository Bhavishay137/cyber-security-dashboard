def calculate_score(password_strength, url_result, scam_result):
    score = 100

    if password_strength == "Weak":
        score -= 30
    elif password_strength == "Moderate":
        score -= 15

    if "Unsafe" in url_result:
        score -= 30
    elif "Suspicious" in url_result:
        score -= 15

    if "Scam" in scam_result:
        score -= 30
    elif "Suspicious" in scam_result:
        score -= 15

    return max(score, 0)