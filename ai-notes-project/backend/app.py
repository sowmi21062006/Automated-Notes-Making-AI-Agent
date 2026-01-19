from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend to talk to backend

@app.route("/")
def home():
    return "Backend is running successfully ✅"

# TEXT → NOTES
@app.route("/generate_notes", methods=["POST"])
def generate_notes():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    sentences = [s.strip() for s in text.split(".") if s.strip()]

    key_points = sentences[:5]
    summary = ". ".join(sentences[:6]) + "."
    conclusion = "This content gives a clear understanding of the topic and helps in quick revision."

    return jsonify({
        "key_points": key_points,
        "summary": summary,
        "conclusion": conclusion
    })

# AUDIO → NOTES (demo)
@app.route("/audio_notes", methods=["POST"])
def audio_notes():
    return jsonify({
        "key_points": [
            "Audio topic identified",
            "Important concepts extracted",
            "Key ideas summarized"
        ],
        "summary": "The uploaded audio was processed and converted into meaningful notes.",
        "conclusion": "Audio-based notes are ready for learning and revision."
    })

if __name__ == "__main__":
    app.run(debug=True)