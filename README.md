# 🧑‍💻 Mo Ariz — AI-Powered Personal Portfolio

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?style=flat&logo=flask)
![Groq AI](https://img.shields.io/badge/Groq-LLaMA%203.1-orange?style=flat)
![Render](https://img.shields.io/badge/Deployed-Render-purple?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

> A modern, AI-powered personal portfolio website built with **Python Flask** as the backend and **pure HTML, CSS, Vanilla JavaScript** as the frontend. Features a live AI chatbot powered by **Groq's LLaMA 3.1** model that answers questions about me in real-time.

🌐 **Live Demo:** [https://ariz-portfolio.onrender.com](https://ariz-portfolio.onrender.com)

---

## ✨ Features

- 🤖 **AI Chat Assistant** — Powered by Groq (LLaMA 3.1 8B Instant), answers questions about me just like I would
- 📊 **9 Real Projects** — With GitHub links and tech stack badges
- 🏆 **10+ Certificates** — Microsoft Azure, Oracle OCI, and more
- 🎓 **Education & Internships** — Full academic and experience timeline
- 🛠️ **Skills Section** — Organized by category with hover effects
- 📄 **Resume Download** — Direct link to CV via Google Drive
- 📱 **Fully Responsive** — Works on all screen sizes
- 🌙 **Dark Theme UI** — Modern dark green aesthetic
- 🔒 **Secure API** — API key never exposed to the browser

---

## 🗂️ Project Structure

```
portfolio/
│
├── app.py                  ← Flask backend (Groq API calls handled here)
├── .env                    ← Secret API key (never commit this!)
├── .gitignore              ← Ignores .env, venv, cache files
├── requirements.txt        ← Python dependencies
├── README.md               ← Project documentation
│
├── static/
│   ├── profile.png         ← Profile photo
│   └── Mo_Ariz_CV.pdf      ← Resume file
│
└── templates/
    └── index.html          ← Complete portfolio frontend (HTML + CSS + JS)
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Backend | Python 3.12, Flask | Server, routing, API calls |
| Frontend | HTML5, CSS3, Vanilla JS | UI, animations, chat logic |
| AI Model | Groq API (LLaMA 3.1 8B) | AI chatbot responses |
| Deployment | Render (Free Tier) | Live hosting |
| Version Control | Git, GitHub | Source code management |

---

## ⚙️ How It Works

```
User types message in chat
        ↓
JavaScript sends POST request to /chat
        ↓
Flask receives request
        ↓
Flask adds PERSONA (Mo's profile) + conversation history
        ↓
Groq API call (LLaMA 3.1 model)
        ↓
AI generates reply as Mo Ariz
        ↓
Flask returns JSON response
        ↓
JavaScript displays message in chat UI
```

---

## 🚀 Getting Started (Local Setup)

### 1. Clone the repository
```bash
git clone https://github.com/9ariz1/Ariz_portfolio.git
cd Ariz_portfolio
```

### 2. Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Get your free Groq API key
- Go to [console.groq.com](https://console.groq.com)
- Sign up → Create API Key (completely free!)

### 5. Add API key to app.py
```python
GROQ_API_KEY = "gsk_your_api_key_here"
```

### 6. Run the app
```bash
py app.py
```

### 7. Open in browser
```
http://127.0.0.1:5000
```

---

## 📦 Requirements

```
flask
flask-cors
requests
python-dotenv
gunicorn
```

Install all:
```bash
pip install -r requirements.txt
```

---

## 🤖 AI Chat Feature

The **"Ask Me Anything"** section uses **Groq's LLaMA 3.1 8B Instant** model:

- ⚡ Extremely fast responses
- 🆓 Completely free — no credit card required
- 🇮🇳 Works in India
- 📊 30 requests/minute, 14,400 requests/day

The AI is pre-loaded with a full persona containing Mo's skills, projects, internships, education, and personality — so it answers just like Mo would!

---

## 📁 Projects Showcase

| # | Project | Tech Stack | Status |
|---|---------|-----------|--------|
| 1 | Real-Time Object Detection | Python, CNN, OpenCV | ✅ Complete |
| 2 | Course Recommendation System | Scikit-learn, Streamlit | ✅ Complete |
| 3 | AI-Based Disease Prediction | Django, ML, Pickle | ✅ Complete |
| 4 | Gamma Squeeze Orchestrator | Pandas, yfinance, Streamlit | ✅ Complete |
| 5 | Real-Time Weather Forecast App | Flask, OpenWeatherMap API | ✅ Complete |
| 6 | Real-Time Face Detection | OpenCV, Haar Cascade | ✅ Complete |
| 7 | Amazon Global Sales Dashboard | Power BI, DAX | ✅ Complete |
| 8 | Smart Attendance System | OpenCV, Face Recognition | 🚧 In Progress |
| 9 | HireHub — Job Portal | Django, SQL | 🚧 In Progress |

---

## 🏆 Certifications

- Microsoft Azure Fundamentals
- Oracle Cloud Infrastructure 2025 — Data Science Professional
- Data Analytics — Integral University
- SQL and Relational Databases 101 — Cognitive Class
- And more...

---

## 🌐 Deployment (Render)

This project is deployed on **Render Free Tier**:

1. Push code to GitHub
2. Connect GitHub repo to Render
3. Set environment variable: `GROQ_API_KEY`
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `gunicorn app:app`
6. Deploy! 🚀

> ⚠️ Free tier sleeps after 15 min of inactivity — first load may take 50 seconds

---

## 📬 Contact

| Platform | Link |
|----------|------|
| 📧 Email | mohammadariz98765@gmail.com |
| 📱 Phone | +91 93051 78391 |
| 💼 LinkedIn | [linkedin.com/in/mo-ariz](https://www.linkedin.com/in/mo-ariz/) |
| 🐙 GitHub | [github.com/9ariz1](https://github.com/9ariz1) |
| 🌐 Portfolio | [ariz-portfolio.onrender.com](https://ariz-portfolio.onrender.com) |

---

## ⚠️ Important Notes

- Never push API key to GitHub
- Use environment variables for production
- `.env` file is listed in `.gitignore`
- For local development, hardcode key in `app.py` only

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with ❤️ by Mo Ariz — 2026*

⭐ **If you found this helpful, please give it a star!**
