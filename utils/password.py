import re
import random
import string


# 🔍 CHECK PASSWORD STRENGTH
def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[@#$%^&+=]", password):
        score += 1

    strength_levels = ["Weak", "Moderate", "Strong", "Very Strong"]
    return strength_levels[min(score, 3)]


# ⏳ SMART CRACK TIME (ONLY ONE UNIT)
def crack_time(password):
    guesses = 94 ** len(password)
    seconds = int(guesses / 1e9)

    if seconds < 60:
        return f"{seconds} seconds"

    minutes = seconds // 60
    if minutes < 60:
        return f"{minutes} minutes"

    hours = minutes // 60
    if hours < 24:
        return f"{hours} hours"

    days = hours // 24
    if days < 30:
        return f"{days} days"

    months = days // 30
    if months < 12:
        return f"{months} months"

    years = months // 12
    return f"{years} years"


# 💡 SUGGEST STRONG PASSWORD
def suggest_password(password):
    chars = string.ascii_letters + string.digits + "@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(12))


# ✅ USABILITY CHECK
def usability(strength):
    if strength == "Weak":
        return "❌ Not Safe"
    elif strength == "Moderate":
        return "⚠️ Risky"
    else:
        return "✅ Safe"


# 🔐 GENERATE STRONG PASSWORD
def generate_password():
    chars = string.ascii_letters + string.digits + "@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(14))