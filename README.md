<h1 align="center">🔐 Cyber Security Dashboard</h1>

<p align="center">
A web-based tool to check your digital safety by analyzing passwords, websites, and messages.
</p>

<hr>

<h2>🧠 What is this Project?</h2>

<p>
The <b>Cyber Security Dashboard</b> is a simple and practical web application that helps users understand how safe they are online.
</p>

<p>
It allows users to:
<br>🔐 Check password strength
<br>🌐 Analyze website safety
<br>📧 Detect scam messages
<br>🧠 Get a Cyber Safety Score (0–100)
</p>

<hr>

<h2>🚀 How I Built This Project</h2>

<p><b>Step 1: Setup</b><br>
- Created project folder<br>
- Installed Python & Flask<br>
- Created <code>app.py</code>
</p>

<p><b>Step 2: First Flask App</b><br>
- Ran server and displayed "Hello World"
</p>

<p><b>Step 3: HTML Integration</b><br>
- Created <code>templates</code> folder<br>
- Added <code>index.html</code><br>
- Connected using <code>render_template()</code>
</p>

<p><b>Step 4: Form Handling</b><br>
- Added inputs (password, URL, message)<br>
- Used POST method<br>
- Captured using <code>request.form</code>
</p>

<p><b>Step 5: Feature Development</b><br>
- Password checker<br>
- URL checker<br>
- Scam detector
</p>

<p><b>Step 6: Score System</b><br>
- Combined results into cyber safety score
</p>

<p><b>Step 7: UI Improvements</b><br>
- Styled using CSS<br>
- Added clean layout
</p>

<p><b>Step 8: Recommendations</b><br>
- Added user suggestions
</p>

<hr>

<h2>⚠️ Errors Faced & Fixes</h2>

<p><b>❌ TemplateNotFound Error</b><br>
Flask couldn't find <code>index.html</code><br>
✔ Fixed by placing it inside <code>templates</code> folder
</p>

<p><b>❌ Git Push Rejected</b><br>
Error: <code>main -> main (fetch first)</code><br>
✔ Fixed using:
<pre>git pull origin main --rebase</pre>
Then pushing again
</p>

<p><b>❌ Merge Error</b><br>
Error: <code>MERGE_HEAD exists</code><br>
✔ Fixed using:
<pre>git commit -m "Merged changes"</pre>
</p>

<p><b>❌ File Extension Issue</b><br>
Files were saved as .txt<br>
✔ Fixed by enabling file extensions
</p>

<hr>

<h2>🌐 Deployment (Render)</h2>

<p><b>Step 1: Added Deployment Files</b></p>
<pre>
requirements.txt
Procfile
</pre>

<p><b>requirements.txt:</b></p>
<pre>
flask
gunicorn
</pre>

<p><b>Procfile:</b></p>
<pre>
web: gunicorn app:app
</pre>

<p><b>Step 2: Updated app.py</b></p>
<pre>
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
</pre>

<p><b>Step 3: Pushed Code to GitHub</b></p>

<p><b>Step 4: Deployed using Render</b><br>
- Connected GitHub repo<br>
- Selected Python environment<br>
- Build command:
<pre>pip install -r requirements.txt</pre>
- Start command:
<pre>gunicorn app:app</pre>
</p>

<p>
After deployment, the app is available as a live website 🌐
</p>

<hr>

<h2>✨ Features</h2>

<p>
🔐 Password Strength Analyzer<br>
🌐 Website Safety Checker<br>
📧 Scam Message Detector<br>
🧠 Cyber Safety Score<br>
🔧 Smart Recommendations
</p>

<hr>

<h2>🛠️ Tech Stack</h2>

<p>
Python<br>
Flask<br>
HTML<br>
CSS
</p>

<hr>

<h2>📂 Project Structure</h2>

<pre>
cyber-dashboard/
│
├── app.py
├── requirements.txt
├── Procfile
├── templates/
│     └── index.html
├── utils/
│     ├── password.py
│     ├── url_checker.py
│     ├── scam_detector.py
│     └── score.py
</pre>

<hr>

<h2>⚙️ How to Run</h2>

<pre>
pip install flask
python app.py
</pre>

<p>
Open in browser:<br>
http://127.0.0.1:5000/
</p>

<hr>

<h2>🎯 What I Learned</h2>

<p>
- Flask fundamentals<br>
- Full-stack basics<br>
- Debugging real errors<br>
- Git & GitHub workflow<br>
- Deployment process
</p>

<hr>

<h2>👨‍💻 About Me</h2>

<p>
Hi, I’m <b>Bhavi Bishnoi</b> 👋<br>
Exploring cybersecurity and development.
</p>

<hr>

<h2>🙌 Final Note</h2>

<p>
This project helped me understand how real-world applications are built, debugged, and deployed.
</p>
