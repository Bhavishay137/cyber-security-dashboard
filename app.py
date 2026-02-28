from flask import Flask, render_template, request
from utils.password import check_password, crack_time, suggest_password, usability, generate_password
from utils.url_checker import check_url
from utils.scam_detector import detect_scam

# ✅ NEW IMPORT
from utils.score import password_score, url_score, message_score

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


# PASSWORD
@app.route("/password", methods=["GET", "POST"])
def password():
    data = None
    generated = None
    score = None   # ✅ NEW

    if request.method == "POST":
        password = request.form.get("password")

        if "generate" in request.form:
            generated = generate_password()

        if password:
            strength = check_password(password)

            data = {
                "strength": strength,
                "crack": crack_time(password),
                "suggestion": suggest_password(password),
                "use": usability(strength)
            }

            score = password_score(strength)   # ✅ NEW

    return render_template("password.html", data=data, generated=generated, score=score)


# URL
@app.route("/url", methods=["GET", "POST"])
def url():
    data = None
    score = None   # ✅ NEW

    if request.method == "POST":
        url = request.form.get("url")
        if url:
            data = check_url(url)
            score = url_score(data)   # ✅ NEW

    return render_template("url.html", data=data, score=score)


# MESSAGE
@app.route("/message", methods=["GET", "POST"])
def message():
    data = None
    score = None   # ✅ NEW

    if request.method == "POST":
        message = request.form.get("message")
        if message:
            data = detect_scam(message)
            score = message_score(data)   # ✅ NEW

    return render_template("message.html", data=data, score=score)


if __name__ == "__main__":
    app.run(debug=True)