import re

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

    strength = ["Weak", "Moderate", "Strong", "Very Strong"]

    return strength[min(score, 3)]