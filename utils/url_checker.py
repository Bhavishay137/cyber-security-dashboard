def check_url(url):
    if not url:
        return "No URL provided"

    if not url.startswith("https"):
        return "⚠️ Unsafe (No HTTPS)"

    if "login" in url or "verify" in url:
        return "⚠️ Suspicious (Phishing keywords detected)"

    return "✅ Safe Website"