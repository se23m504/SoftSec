import os

from flask import Flask, send_file, redirect, url_for
from flask_httpauth import HTTPDigestAuth
from waitress import serve
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
print(os.getenv('FLASK_SECRET_KEY'))
app.secret_key = os.getenv('FLASK_SECRET_KEY')

auth = HTTPDigestAuth()

users = {
    'se23m504': 'password123',
}

@app.route('/')
def index():
    return send_file('index.html')

@auth.get_password
def get_password(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/protected')
@auth.login_required
def digest_protected():
    return send_file('protected.html')

@app.route('/logout')
def logout():
    resp = redirect(url_for('index'))
    resp.set_cookie('session', '', expires=0)
    return resp

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8000)
