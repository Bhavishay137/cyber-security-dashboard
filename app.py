from flask import Flask, render_template, request
from utils.password import check_password, crack_time
from utils.url_checker import check_url
from utils.scam_detector import detect_scam
from utils.score import calculate_score

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    strength = None
    crack = None
    url_result = None
    scam_result = None
    final_score = None
    recommendations = []

    if request.method == "POST":
        password = request.form.get("password")
        url = request.form.get("url")
        message = request.form.get("message")

        strength = check_password(password)
        crack = crack_time(password)
        url_result = check_url(url)
        scam_result = detect_scam(message)

        final_score = calculate_score(strength, url_result, scam_result)

        if strength == "Weak":
            recommendations.append("Use stronger password")

        if "Unsafe" in url_result or "Risk" in url_result:
            recommendations.append("Avoid suspicious websites")

        if "Scam" in scam_result:
            recommendations.append("Do not trust unknown messages")

    return render_template("index.html",
                           strength=strength,
                           crack=crack,
                           url_result=url_result,
                           scam_result=scam_result,
                           final_score=final_score,
                           recommendations=recommendations)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)