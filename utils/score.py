def password_score(strength):
    if strength == "Very Strong":
        return 95
    elif strength == "Strong":
        return 75
    elif strength == "Moderate":
        return 50
    else:
        return 20


def url_score(url_data):
    if not url_data:
        return 0

    status = url_data.get("status", "")

    if "HIGH RISK" in status:
        return 20
    elif "SUSPICIOUS" in status:
        return 50
    else:
        return 90


def message_score(message_data):
    if not message_data:
        return 0

    risk = message_data.get("risk", 0)
    return max(100 - risk, 0)