from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Example route
@app.route("/")
def home():
    return {"message": "Dolphin backend is running!"}

# Proxy endpoint to call LM Studio or Ollama later
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    # For now, just echo back
    return jsonify({"reply": f"You said: {user_message}"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
