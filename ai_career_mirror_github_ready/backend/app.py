from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os, requests

app = Flask(__name__, static_folder='../frontend', static_url_path='/')
CORS(app)

# Gemini-only: read GEMINI_API_KEY from env variable
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')  # MUST be set for production use

def call_gemini(prompt):
    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY environment variable is not set. See README.")
    headers = {'Content-Type': 'application/json'}
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    resp = requests.post(url, params={'key': GEMINI_API_KEY}, headers=headers, json=payload, timeout=30)
    resp.raise_for_status()
    body = resp.json()
    # Extract text safely
    try:
        return body['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        raise RuntimeError(f"Unexpected Gemini response structure: {e} - {body}")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json() or {}
    name = data.get('name','').strip()
    skills = data.get('skills','').strip()
    interests = data.get('interests','').strip()
    education = data.get('education','').strip()

    prompt = f"""You are a helpful career advisor AI.
Based on the following information, suggest the best suitable career by 2026 in India.
Provide a clear JSON-like response with keys: job_title, salary_range, top_cities (list), advice (list of strings), and a short motivational line.

User info:
Name: {name}
Skills: {skills}
Interests: {interests}
Education: {education}

Keep the answer concise and structured.
"""

    try:
        ai_text = call_gemini(prompt)
        # Return raw ai_text in 'result' so frontend can display. For more structure, parse the text.
        return jsonify({'result': ai_text})
    except Exception as e:
        return jsonify({'error': 'AI call failed', 'details': str(e)}), 500

# Serve frontend file (optional)
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
