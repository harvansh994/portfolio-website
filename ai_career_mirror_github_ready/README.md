# AI Career Mirror — GitHub-ready (Gemini-only)

**Author:** Harvansh Pathak

This repository contains a full-stack demo app (frontend + backend) that predicts a likely career using **Google's Gemini** generative API.

## What you'll find
- `frontend/` — static website (index.html, style.css, script.js)
- `backend/` — Flask backend (`app.py`) that calls Gemini (requires GEMINI_API_KEY)
- `.gitignore` — recommended ignores
- `LICENSE` — MIT license
- `.env.example` — example environment variables
- `README.md` — this file

## Quick setup (local)
1. Clone the repo and navigate into it:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-career-mirror.git
   cd ai-career-mirror
   ```
2. Create a Python virtual environment and install deps:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Add your Gemini API key:
   ```bash
   export GEMINI_API_KEY=your_key_here    # macOS/Linux
   set GEMINI_API_KEY=your_key_here       # Windows (cmd)
   ```
   Or create a `.env` file and load it before running.
4. Run the backend:
   ```bash
   python app.py
   ```
5. Open `frontend/index.html` in a browser, or navigate to `http://localhost:5000` to use the served frontend.

## Deploying (Render + Netlify)
- Deploy `backend/` on Render (set GEMINI_API_KEY env var)
- Deploy `frontend/` on Netlify and point `script.js` fetch URL to your Render backend `/predict` endpoint.
See the detailed steps in the earlier conversation for a free deployment pipeline.
