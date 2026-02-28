import re
from urllib.parse import urlparse

def check_url(url):
    parsed = urlparse(url)
    domain = parsed.netloc

    issues = []
    threats = []
    score = 0

    if not url.startswith("https"):
        issues.append("No HTTPS")
        threats.append("Data interception risk")
        score += 2

    if len(url) > 60:
        issues.append("URL too long")
        threats.append("Hidden malicious parameters")
        score += 1

    if re.search(r"\d+\.\d+\.\d+\.\d+", domain):
        issues.append("IP-based URL")
        threats.append("Possible phishing/malware")
        score += 2

    keywords = ["login", "verify", "bank", "secure"]
    for word in keywords:
        if word in url.lower():
            issues.append(f"Suspicious keyword: {word}")
            threats.append("Credential phishing attempt")
            score += 1

    if score >= 4:
        status = "🚨 HIGH RISK"
    elif score >= 2:
        status = "⚠️ SUSPICIOUS"
    else:
        status = "✅ SAFE"

    return {
        "status": status,
        "domain": domain,
        "issues": issues,
        "threats": threats
    }