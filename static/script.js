function showResult(text, isError = false) {
  const resultDiv = document.getElementById("result");
  resultDiv.innerText = text;
  if (isError) {
    resultDiv.classList.add("error");
  } else {
    resultDiv.classList.remove("error");
  }
}

async function encrypt() {
  const message = document.getElementById("message").value.trim();
  const key = document.getElementById("key").value.trim();
  if (!message || !key) {
    showResult("Please enter both message and key.", true);
    return;
  }
  showResult("Encrypting...");
  try {
    const res = await fetch("http://127.0.0.1:5000/encrypt", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message, key }),
    });
    if (!res.ok) throw new Error("Server error");
    const data = await res.json();
    showResult("Encrypted: " + data.encrypted);
  } catch (err) {
    showResult("Encryption failed. Is the backend running?", true);
  }
}

async function decrypt() {
  const cipher = document.getElementById("message").value.trim();
  const key = document.getElementById("key").value.trim();
  if (!cipher || !key) {
    showResult("Please enter both cipher text and key.", true);
    return;
  }
  showResult("Decrypting...");
  try {
    const res = await fetch("http://127.0.0.1:5000/decrypt", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ cipher, key }),
    });
    if (!res.ok) throw new Error("Server error");
    const data = await res.json();
    showResult("Decrypted: " + data.decrypted);
  } catch (err) {
    showResult("Decryption failed. Is the backend running?", true);
  }
}
