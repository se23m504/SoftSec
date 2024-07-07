import re
import random
from flask import Flask, request, jsonify, send_file
from waitress import serve

app = Flask(__name__)

def regex_to_alphabet(regex):
    ranges = re.findall(r'\[([^\]]+)\]', regex)
    if not ranges:
        return None
    
    range_str = ranges[0]
    alphabet = ''
    i = 0
    while i < len(range_str):
        start = range_str[i]
        if i + 2 < len(range_str) and range_str[i + 1] == '-':
            end = range_str[i + 2]
            for char_code in range(ord(start), ord(end) + 1):
                alphabet += chr(char_code)
            i += 3
        else:
            alphabet += start
            i += 1
    
    return alphabet

def generate_password(alphabet, length):
    password = ''.join(random.choice(alphabet) for _ in range(length))
    return password

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/generate', methods=['POST'])
def generate_passwords():
    data = request.json
    alphabet_regex = data.get('alphabetRegex', r'[a-zA-Z0-9]')
    num_passwords = int(data.get('numPasswords', 1))
    password_length = int(data.get('passwordLength', 12))

    alphabet = regex_to_alphabet(alphabet_regex)
    if not alphabet:
        return jsonify(error='Invalid alphabet regex pattern'), 400

    passwords = []
    for _ in range(num_passwords):
        password = generate_password(alphabet, password_length)
        passwords.append(password)

    return jsonify(passwords=passwords)

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8000)
