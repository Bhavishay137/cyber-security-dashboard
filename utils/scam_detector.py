def detect_scam(message):
    if not message:
        return "No message"

    keywords = ["urgent", "win", "prize", "click", "verify", "bank", "password"]

    score = sum(word in message.lower() for word in keywords)

    if score >= 3:
        return "🚨 Scam Detected (High Risk)"
    elif score == 2:
        return "⚠️ Suspicious Message"
    else:
        return "✅ Safe Message"