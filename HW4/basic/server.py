from flask import Flask, send_file, jsonify, request, redirect, url_for
from waitress import serve

app = Flask(__name__)

users = {
    'se23m504': {'password': 'password123'},
}

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username]['password'] == password:
        return jsonify({ 'username': username }), 201
    else:
        return "Invalid username or password", 401

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8000)
