# 🧑‍💻 Mo Ariz — Personal Portfolio Website

An AI-powered personal portfolio website built with **Flask** and **Groq AI**, showcasing my skills, projects, internships, and experience as an entry-level Data Scientist, Data Analyst, and Python Developer.

---

## 🌟 Features

- ⚡ **AI Chat Assistant** — Powered by Groq (LLaMA 3.1), answers questions about me in real-time
- 📊 **Projects Showcase** — 9 real-world projects with GitHub links
- 🎓 **Education & Internships** — Full academic and experience timeline
- 🛠️ **Skills Section** — Organized by category
- 📄 **Resume Download** — Direct link to CV
- 📱 **Responsive Design** — Works on all screen sizes
- 🌙 **Dark Mode UI** — Modern dark green theme

---

## 🗂️ Project Structure

```
portfolio/
│
├── app.py                  ← Flask backend (Groq API calls)
├── .env                    ← Secret API key (never share!)
├── .gitignore              ← Ignores .env and cache files
├── requirements.txt        ← Python dependencies
│
├── static/
│   └── profile.png         ← Profile photo
│
└── templates/
    └── index.html          ← Full portfolio frontend
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask, Flask-CORS |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| AI Model | Groq API (LLaMA 3.1 8B Instant) |
| Styling | CSS Variables, Glassmorphism, Dark Theme |
| Deployment | Local / Railway / Render |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/9ariz1/portfolio.git
cd portfolio
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

### 4. Add your Groq API key
Get your free API key from [console.groq.com](https://console.groq.com)

Open `app.py` and set your key:
```python
GROQ_API_KEY = "gsk_your_api_key_here"
```

### 5. Run the app
```bash
py app.py
```

### 6. Open in browser
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
```

Install all with:
```bash
pip install flask flask-cors requests python-dotenv
```

---

## 🤖 AI Chat Feature

The **"Ask Me Anything"** section uses **Groq's LLaMA 3.1 8B Instant** model — completely free with generous limits:

- 30 requests/minute
- 14,400 requests/day
- No credit card required ✅

The AI is pre-loaded with Mo's full persona — skills, projects, internships, and personality — so it answers questions just like Mo would.

---

## 📁 Projects Included

| # | Project | Tech | Status |
|---|---------|------|--------|
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

## 📬 Contact

| Platform | Link |
|----------|------|
| 📧 Email | mohammadariz98765@gmail.com |
| 📱 Phone | +91 93051 78391 |
| 💼 LinkedIn | [linkedin.com/in/mo-ariz](https://www.linkedin.com/in/mo-ariz/) |
| 🐙 GitHub | [github.com/9ariz1](https://github.com/9ariz1) |

---

## ⚠️ Important

- Never push your API key to GitHub
- Add `GROQ_API_KEY` to `.gitignore` or use environment variables on deployment
- For production deployment use **Railway** or **Render**

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with ❤️ by Mo Ariz — 2026*