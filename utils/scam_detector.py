def detect_scam(message):
    keywords = ["urgent", "win", "click", "verify", "bank"]

    found = [k for k in keywords if k in message.lower()]
    risk = len(found) * 20

    if risk >= 60:
        status = "🚨 High Risk"
    elif risk >= 30:
        status = "⚠️ Suspicious"
    else:
        status = "✅ Safe"

    return {
        "status": status,
        "risk": min(risk, 100)
    }