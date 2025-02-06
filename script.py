from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# OpenAI API key setup
openai.api_key = "sk_6d2350dc4494e8443199e0923b1598df3d7998e882b400d2"

@app.route('/generate-voice', methods=['POST'])
def generate_voice():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "Text is required"}), 400

    try:
        response = openai.audio.speech.create(
            model="tts-1",
            voice="alloy",  # Alloy, Echo, Fable, Onyx, Nova, Shimmer
            input=text
        )

        audio_file = "output.mp3"
        response.stream_to_file(audio_file)

        return jsonify({"message": "Success", "audio_url": f"/static/{audio_file}"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
