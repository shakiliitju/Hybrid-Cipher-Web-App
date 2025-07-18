from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import string


app = Flask(__name__, template_folder='templates')
CORS(app)


def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return("".join(key)) 
    else: 
        for i in range(len(string) - len(key)): 
            key.append(key[i % len(key)]) 
    return("".join(key))

def vigenereEncrypt(text, key): 
    cipher_text = [] 
    for i in range(len(text)): 
        if text[i] in string.ascii_uppercase:
            x = (ord(text[i]) + ord(key[i])) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        else:
            cipher_text.append(text[i]) 
    return "".join(cipher_text) 

def vigenereDecrypt(cipher_text, key): 
    orig_text = [] 
    for i in range(len(cipher_text)): 
        if cipher_text[i] in string.ascii_uppercase:
            x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
            x += ord('A')
            orig_text.append(chr(x))
        else:
            orig_text.append(cipher_text[i]) 
    return "".join(orig_text) 

polybius_square = {
    'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
    'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '24', 'K': '25',
    'L': '31', 'M': '32', 'N': '33', 'O': '34', 'P': '35',
    'Q': '41', 'R': '42', 'S': '43', 'T': '44', 'U': '45',
    'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55'
}
reverse_polybius_square = {v: k for k, v in polybius_square.items()}

def polybiusEncrypt(text):
    text = text.upper().replace('J', 'I')
    cipher = ''
    for char in text:
        if char in polybius_square:
            cipher += polybius_square[char]
        else:
            cipher += char
    return cipher

def polybiusDecrypt(cipher):
    text = ''
    i = 0
    while i < len(cipher):
        if cipher[i].isdigit() and i+1 < len(cipher) and cipher[i+1].isdigit():
            pair = cipher[i] + cipher[i+1]
            text += reverse_polybius_square.get(pair, '')
            i += 2
        else:
            text += cipher[i]
            i += 1
    return text

def hybridEncrypt(plain_text, key):
    key = key.upper()
    plain_text = plain_text.upper().replace('J', 'I')
    vigenere_key = generateKey(plain_text, key)
    vigenere_encrypted = vigenereEncrypt(plain_text, vigenere_key)
    polybius_encrypted = polybiusEncrypt(vigenere_encrypted)
    return polybius_encrypted

def hybridDecrypt(cipher_text, key):
    key = key.upper()
    vigenere_encrypted = polybiusDecrypt(cipher_text)
    vigenere_key = generateKey(vigenere_encrypted, key)
    decrypted = vigenereDecrypt(vigenere_encrypted, vigenere_key)
    return decrypted



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    message = data.get('message', '')
    key = data.get('key', '')
    encrypted = hybridEncrypt(message, key)
    return jsonify({'encrypted': encrypted})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    cipher = data.get('cipher', '')
    key = data.get('key', '')
    decrypted = hybridDecrypt(cipher, key)
    return jsonify({'decrypted': decrypted})

if __name__ == '__main__':
    app.run(debug=True)