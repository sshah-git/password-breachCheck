# password-breachCheck
🔐 Password Breach Checker

A simple and secure web application that checks whether a password has been exposed in known data breaches using the k-Anonymity model from the Have I Been Pwned API.

🚀 Overview

This project allows users to safely check if their password has been compromised—without ever sending the full password over the internet.

Instead of transmitting the entire password, the app:

Hashes the password using SHA-1
Sends only the first 5 characters of the hash to the API
Compares the remaining hash locally

This ensures privacy while still leveraging a massive breach database.

🧠 How It Works

User inputs a password
Password is hashed using SHA-1
Hash is split into:
Prefix (first 5 chars) → sent to API
Suffix (remaining chars) → kept locally
API returns a list of matching hash suffixes
App checks if the suffix exists → returns breach count

✨ Features

🔒 Privacy-first password checking (k-anonymity)
⚡ Fast API-based lookup
🌐 Simple Flask web interface
📊 Returns how many times a password has been seen in breaches
✅ Clear user feedback (safe vs compromised)
🛠️ Tech Stack
Backend: Python, Flask
Security: SHA-1 hashing (hashlib)
API: Have I Been Pwned (Pwned Passwords API)
HTTP Requests: requests


⚙️ Installation & Setup
1. Clone the repo
git clone https://github.com/your-username/password-breach-checker.git
cd password-breach-checker
2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3. Install dependencies
pip install flask requests
4. Run the app
python app.py
5. Open in browser
http://127.0.0.1:5000/

🔍 Example Output
⚠️ WARNING: This password has appeared 1,234,567 times in data breaches
✅ Good news! This password has not been found in known breaches
🔐 Security Notes
Passwords are never stored
Full hashes are never sent externally
Uses k-anonymity to protect user data
Relies on a trusted public breach database
💡 Future Improvements
Add password strength analysis (entropy, patterns)
Implement rate limiting / caching
Improve UI/UX (React frontend 👀)
Add dark mode (because obviously)
Deploy to cloud (Render / AWS / Vercel)
📌 Why This Project Matters

With billions of leaked credentials online, password reuse is one of the biggest security risks. This project demonstrates:

Real-world API integration
Secure system design principles
Practical cybersecurity awareness
👤 Author

Sana Shah
Computer Science Student
Interested in healthcare, cybersecurity, and building impactful tech
