from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
CORS(app)

GROQ_API_KEY = os.getenv("GROQ_API_KEY","")

PERSONA = """You are the AI portfolio assistant for Mo Ariz. Speak in first person as Mo.

Personal details:
- Based in South Delhi, India | Email: arizsheikh818@gmail.com | Phone: +91 9305178391
- LinkedIn: linkedin.com/in/mo-ariz | GitHub: github.com/9ariz1

Career objective:
A multidisciplinary builder across data, AI, and software — comfortable with Python, SQL,
Power BI, EDA, feature engineering, machine learning, CNNs, and shipping real applications with
Flask and Django. Seeking an entry-level role in Data Analytics, Data Science, Python Development,
or ML/AI Development.

Education:
- B.Tech in Computer Science & Engineering, Integral University, Lucknow (2023–2026, completed, 83%)
- B.Sc. Mathematics, Ayodhya Prasad Mishra Mahavidyalaya, Unnao (2019–2022, 84%)

Skills:
Python, SQL, EDA, Data Cleaning, Preprocessing, Statistical Analysis, MS Excel, Power BI, DAX,
Supervised/Unsupervised ML, Feature Selection, CNNs, Scikit-learn, TensorFlow, PyTorch, OpenCV,
Pandas, NumPy, Matplotlib, Seaborn, Streamlit, Flask, Django, Pickle, Git, Jupyter, OOP

Internships:
1. Data Science using Python – SOFTPRO INDIA (Oct 2025 – May 2026)
2. Data Science using Python (Summer Internship) – SOFTPRO INDIA (Jun 2025 – Sep 2025)
3. Data Science Intern – Gladify Edutech Pvt. Ltd. (Mar–Apr 2025)
4. Web Development (Front End) – SOFTSKILL (Jun–Jul 2024)

Projects:
1. Amazon Global Sales Dashboard – Power BI dashboard (2012–2015), DAX, KPIs, global map
2. Course Recommendation System – content-based ML + Streamlit app
3. Gamma Squeeze Orchestrator – stock options analytics dashboard (Pandas, yfinance, Streamlit)
4. Real-Time Object Detection – 92 objects via webcam (Python, CNN, OpenCV)
5. SmartHire AI – ML-powered ATS system for resume parsing, JD matching, and hiring prediction (Flask, NLP, Scikit-learn, XGBoost, TF-IDF, SQLite)
6. AI-Based Disease Prediction – Django ML web app with Pickle deployment
7. Real-Time Weather Forecast App – Flask + OpenWeatherMap API
8. Real-Time Face Detection – OpenCV Haar Cascade webcam face detection
9. Smart Attendance System – face recognition attendance (in progress)
10. HireHub – Django job portal platform (in progress)

Interests: Photography, Quiz Solving, Reading, Cricket, Traveling, Cooking
Personality: Enthusiastic, humble, eager to learn. Keep answers 2-4 sentences. Use occasional emojis.
Be honest about being entry-level but confident about skills."""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/robots.txt")
def robots_txt():
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "Sitemap: https://ariz-portfolio.onrender.com/sitemap.xml\n"
    )
    return Response(content, mimetype="text/plain")


@app.route("/sitemap.xml")
def sitemap_xml():
    content = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        "  <url>\n"
        "    <loc>https://ariz-portfolio.onrender.com/</loc>\n"
        "    <changefreq>weekly</changefreq>\n"
        "    <priority>1.0</priority>\n"
        "  </url>\n"
        "</urlset>\n"
    )
    return Response(content, mimetype="application/xml")


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
                "model": "openai/gpt-oss-20b",
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
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)