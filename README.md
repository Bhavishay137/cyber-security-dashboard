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

<p>
The goal of this project is to make cybersecurity <b>easy, accessible, and understandable</b> for everyone.
</p>

<hr>

<h2>🚀 How I Built This Project</h2>

<p><b>Step 1: Setup</b><br>
- Created project folder<br>
- Installed Python & Flask<br>
- Created <code>app.py</code>
</p>

<p><b>Step 2: First Flask App</b><br>
- Ran a basic server<br>
- Displayed "Hello World"
</p>

<p><b>Step 3: HTML Integration</b><br>
- Created <code>templates</code> folder<br>
- Added <code>index.html</code><br>
- Used <code>render_template()</code>
</p>

<p><b>Step 4: Form Handling</b><br>
- Added input fields<br>
- Used POST method<br>
- Captured data using <code>request.form</code>
</p>

<p><b>Step 5: Password Checker</b><br>
- Created <code>password.py</code><br>
- Implemented strength logic
</p>

<p><b>Step 6: URL Checker</b><br>
- Created <code>url_checker.py</code><br>
- Checked HTTPS & keywords
</p>

<p><b>Step 7: Scam Detector</b><br>
- Created <code>scam_detector.py</code><br>
- Used keyword-based detection
</p>

<p><b>Step 8: Cyber Safety Score</b><br>
- Created <code>score.py</code><br>
- Combined all results
</p>

<p><b>Step 9: UI Improvement</b><br>
- Added styling using CSS<br>
- Improved layout
</p>

<p><b>Step 10: Recommendations</b><br>
- Added smart suggestions for users
</p>

<hr>

<h2>⚠️ Errors I Faced & Solutions</h2>

<p><b>❌ TemplateNotFound Error</b><br>
Flask couldn’t find <code>index.html</code><br>
<b>✔ Fix:</b> Created <code>templates</code> folder and moved file inside it
</p>

<p><b>❌ GitHub Push Rejected</b><br>
Remote repo had existing files<br>
<b>✔ Fix:</b> Used <code>git pull origin main --allow-unrelated-histories</code>
</p>

<p><b>❌ Merge Issue</b><br>
Merge not completed (MERGE_HEAD)<br>
<b>✔ Fix:</b> Ran <code>git commit</code> then pushed again
</p>

<p><b>❌ File Extension Issue</b><br>
Files saved as .txt<br>
<b>✔ Fix:</b> Enabled file extensions and corrected names
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
- Flask basics<br>
- Frontend + Backend connection<br>
- Handling user input<br>
- Debugging errors<br>
- Using Git & GitHub
</p>

<hr>

<h2>🚀 Future Improvements</h2>

<p>
- AI-based detection<br>
- Live deployment<br>
- Better UI/UX<br>
- Mobile support
</p>

<hr>

<h2>👨‍💻 About Me</h2>

<p>
Hi, I’m <b>Bhavi Bishnoi</b> 👋<br>
Currently learning cybersecurity and development.
</p>

<hr>

<h2>🙌 Final Note</h2>

<p>
This project is a step towards making people more aware of their digital safety.
</p>
