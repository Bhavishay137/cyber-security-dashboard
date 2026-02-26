<h1 align="center">🔐 Cyber Security Dashboard</h1>

<p align="center">
A real-time web-based cybersecurity tool that analyzes passwords, URLs, and messages to evaluate digital safety.
</p>

---

## 🧠 What is this Project?

The **Cyber Security Dashboard** is a full-stack web application built using Flask that helps users understand how secure they are online.

It allows users to:
- 🔐 Analyze password strength  
- ⏳ Estimate how long a password would take to crack  
- 🌐 Check if a website is safe or suspicious  
- 📧 Detect scam or phishing messages  
- 🧠 Get an overall cybersecurity assessment  

The goal of this project is to make cybersecurity **simple, interactive, and useful for everyone**, even non-technical users.

---

## ✨ Features

### 🔐 Password Analyzer
- Evaluates password strength (Weak → Very Strong)  
- Estimates **crack time** based on complexity  
- Helps users understand password security  

---

### 🌐 Advanced URL Analyzer
This system goes beyond basic checks and analyzes:
- HTTPS usage  
- URL length  
- Suspicious keywords  
- IP-based URLs  

---

### 📧 Scam Message Detector
- Detects phishing/scam patterns  
- Uses keyword-based logic  
- Classifies messages into:
  - ✅ Safe  
  - ⚠️ Suspicious  
  - 🚨 High Risk  

---

### 🧠 Cyber Safety Evaluation
- Combines all results  
- Provides an overall risk understanding  

---

### 🎨 Interactive UI
- Card-based layout  
- Clean dark theme  
- Hover effects  
- Mobile responsive  

---

## 🚀 How I Built This Project

### Step 1: Backend Setup
- Created Flask application  
- Handled routing and form data  

---

### Step 2: Frontend Integration
- Built UI using HTML & CSS  
- Connected with Flask templates (Jinja)  

---

### Step 3: Feature Development
- Password strength + crack time  
- Advanced URL risk analysis  
- Scam detection system  

---

### Step 4: Scoring Logic
- Combined all outputs into a unified evaluation system  

---

### Step 5: UI Enhancement
- Designed card-based dashboard  
- Improved interactivity  

---

### Step 6: Deployment
- Uploaded code to GitHub  
- Deployed live using Render  

---

## ⚠️ Challenges Faced

### ❌ Git Push Errors
- Error: `main -> main (fetch first)`  
- Solution: Used  
```bash
git pull origin main --rebase