from flask import Flask, render_template, request
import hashlib
import requests

app = Flask(__name__)

def check_password_breach(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    hashes = (line.split(':') for line in response.text.splitlines())
    for hash_suffix, count in hashes:
        if hash_suffix == suffix:
            return int(count)
    return 0

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        password = request.form['password']
        breach_count = check_password_breach(password)
        if breach_count:
            result = f"⚠️ WARNING: This password has appeared {breach_count} times in data breaches."
        else:
            result = "✅ Good news! This password has not been found in known breaches!"
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)