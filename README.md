# Hybrid Cipher Web App (Vigenère + Polybius)

This project is a simple web application for encrypting and decrypting messages using a hybrid of the Vigenère and Polybius ciphers. It features a Python Flask backend and a modern HTML/CSS/JavaScript frontend.

---

## Features

- Encrypt and decrypt messages using a hybrid cipher (Vigenère + Polybius)
- User-friendly web interface
- Handles spaces and non-alphabetic characters gracefully
- API endpoints for integration

---

## Folder Structure

```
Hybrid-Cipher-Web-App/
├── app.py
├── requirements.txt
└── templates/
    └── index.html
```

---

## Requirements

- Python 3.7+
- pip

---

## Installation

1. **Clone or download this repository.**

   ```bash
    git clone https://github.com/shakiliitju/Hybrid-Cipher-Web-App
    .git
    cd Hybrid-Cipher-Web-App
    pip install flask flask-cors
    ```

3. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

4. **Run the Flask backend:**
    ```
    python app.py
    ```

5. **Open the web app:**
    - Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

---

## Usage

- Enter your message and key in the web form.
- Click **Encrypt** to get the cipher text.
- Paste the cipher text and key, then click **Decrypt** to recover your original message.

---

## API Endpoints

- `POST /encrypt`
    - JSON: `{ "message": "YOUR_MESSAGE", "key": "YOUR_KEY" }`
    - Response: `{ "encrypted": "CIPHER_TEXT" }`
- `POST /decrypt`
    - JSON: `{ "cipher": "CIPHER_TEXT", "key": "YOUR_KEY" }`
    - Response: `{ "decrypted": "ORIGINAL_MESSAGE" }`

---

## Notes

- The cipher only fully supports English letters (A-Z). Spaces and punctuation are preserved but not encrypted.
- Make sure the `templates` folder is in the same directory as `app.py` and contains `index.html`.
- The backend is in `app.py`. The frontend is in `templates/index.html`.
- All dependencies are listed in `requirements.txt`.

---

## License

MIT License
