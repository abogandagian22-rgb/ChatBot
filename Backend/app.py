import os

from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

if load_dotenv is not None:
    load_dotenv()

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
model = None

if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-2.0-flash")


def missing_key_response():
    return jsonify({
        "error": "Gemini API key is not configured on the backend.",
        "hint": "Set GEMINI_API_KEY or GOOGLE_API_KEY in the backend environment, then restart the Flask server."
    }), 503

@app.route("/")
def home():
    return "Flask backend is running! Go to /api/chat to chat."

@app.route("/api/chat", methods=["POST"])
def chat():
    if model is None:
        return missing_key_response()

    data = request.get_json(silent=True) or {}
    contents = data.get("contents")

    if not contents or not isinstance(contents, list):
        messages = data.get("messages")
        if not messages or not isinstance(messages, list):
            return jsonify({"error": "No contents or messages provided, or invalid format."}), 400

        contents = []
        for msg in messages:
            role = "user" if msg.get("sender") == "user" else "model"
            text = msg.get("text", "")

            if role not in ["user", "model"]:
                continue

            contents.append({"role": role, "parts": [{"text": text}]})

    generation_config = data.get("generationConfig") or None

    try:
        if generation_config:
            response = model.generate_content(contents, generation_config=generation_config)
        else:
            response = model.generate_content(contents)
        return jsonify({"reply": response.text})
    except Exception as e:
        error_text = str(e)
        print(f"Error calling Gemini API: {error_text}")

        if "429" in error_text or "quota" in error_text.lower():
            return jsonify({"error": "Gemini quota exceeded. Please try again later or use a key with billing enabled."}), 429

        return jsonify({"error": error_text}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
