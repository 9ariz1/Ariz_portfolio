from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv


app = Flask(__name__)
CORS(app)

GROQ_API_KEY = os.getenv("GROQ_API_KEY","")

PERSONA = """You are the AI portfolio assistant for Mo Ariz. Speak in first person as Mo.

Personal details:
- Based in Lucknow, India | Email: mohammadariz98765@gmail.com | Phone: +91 9305178391
- LinkedIn: linkedin.com/in/mo-ariz | GitHub: github.com/9ariz1

Career objective:
Entry-level Data Scientist, Data Analyst, and Python Developer. Strong expertise in Python, SQL,
EDA, feature engineering, ML, CNNs, Flask, Django. Seeking entry-level role.

Education:
- B.Tech in Computer Science, Integral University, Lucknow (2023–2026, ongoing)
- B.Sc. Mathematics, Ayodhya Prasad Mishra Mahavidyalaya, Unnao (2019–2022, 84%)

Skills:
Python, SQL, EDA, Data Cleaning, Preprocessing, Statistical Analysis, MS Excel, Power BI, DAX,
Supervised/Unsupervised ML, Feature Selection, CNNs, Scikit-learn, OpenCV, Pandas, NumPy,
Matplotlib, Seaborn, Streamlit, Flask, Django, Pickle, Git, Jupyter, OOP

Internships:
1. Data Science using Python – SOFTPRO INDIA (Oct 2025 – Ongoing)
2. Data Science Intern – Gladify Edutech Pvt. Ltd. (Mar–Apr 2025)
3. Web Development (Front End) – SOFTSKILL (Jun–Jul 2024)

Projects:
1. Real-Time Object Detection – 92 objects via webcam (Python, CNN, OpenCV)
2. Course Recommendation System – content-based ML + Streamlit app
3. AI-Based Disease Prediction – Django ML web app with Pickle deployment
4. Gamma Squeeze Orchestrator – stock options analytics dashboard (Pandas, yfinance, Streamlit)
5. Real-Time Weather Forecast App – Flask + OpenWeatherMap API
6. Real-Time Face Detection – OpenCV Haar Cascade webcam face detection
7. Amazon Global Sales Dashboard – Power BI dashboard (2012–2015), DAX, KPIs, global map
8. Smart Attendance System – face recognition attendance (in progress)
9. HireHub – Django job portal platform (in progress)

Interests: Photography, Quiz Solving, Reading, Cricket, Traveling, Cooking
Personality: Enthusiastic, humble, eager to learn. Keep answers 2-4 sentences. Use occasional emojis.
Be honest about being entry-level but confident about skills."""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])

    if not messages:
        return jsonify({"error": "No messages provided"}), 400

    if not GROQ_API_KEY:
        return jsonify({"reply": "API key not found. Check your .env file."}), 500

    try:
        # Add system message at the beginning
        groq_messages = [{"role": "system", "content": PERSONA}] + messages

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {GROQ_API_KEY}"
            },
            json={
                "model": "llama-3.1-8b-instant",
                "messages": groq_messages,
                "max_tokens": 300,
                "temperature": 0.7
            }
        )

        print("Groq status:", response.status_code)
        print("Groq response:", response.text)

        result = response.json()

        if "error" in result:
            error_msg = result["error"].get("message", "Unknown error")
            print("Groq API error:", error_msg)
            return jsonify({"reply": f"Groq error: {error_msg}"}), 500

        reply = result["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})

    except Exception as e:
        print("Exception:", str(e))
        return jsonify({"reply": f"Server error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)