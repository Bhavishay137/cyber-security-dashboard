import re

def check_url(url):
    if not url:
        return "No URL provided"

    score = 0

    if not url.startswith("https"):
        score += 2

    if len(url) > 50:
        score += 1

    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        score += 2

    keywords = ["login", "verify", "bank", "secure", "update"]
    if any(word in url.lower() for word in keywords):
        score += 2

    if score >= 4:
        return "🚨 High Risk URL"
    elif score >= 2:
        return "⚠️ Suspicious URL"
    else:
        return "✅ Safe URL"