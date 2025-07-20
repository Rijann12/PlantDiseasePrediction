from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)
genai.configure(api_key="YOUR_API_KEY")  # Replace with your Gemini API key
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/get_precaution", methods=["POST"])
def get_precaution():
    data = request.get_json()
    disease = data.get("disease")
    prompt = f"What are the prevention and treatment tips for the plant disease called '{disease}'?"
    try:
        response = model.generate_content(prompt)
        return jsonify({"precaution": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5001)
