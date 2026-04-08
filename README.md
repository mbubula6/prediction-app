# 🧠 BehavioGraph: Context-Aware Prediction Engine

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Django](https://img.shields.io/badge/Django-6.0-092E20?logo=django)
![Machine Learning](https://img.shields.io/badge/scikit--learn-Enabled-F7931E?logo=scikit-learn)

**BehavioGraph** is an advanced, context-aware monolithic web application that analyzes behavioral inputs and real-time environmental metadata to generate dynamic psychological predictions. By unifying an interactive frontend with an autonomous machine learning backend, it provides continuous insight into a user's motivational state.

---

## ✨ Core Features

### 🔐 Multi-Tenant Architecture
- Complete user authentication and isolation (Registration, Login, Authorization).
- Users independently build their own database of behavioral history.

### 🤖 Intelligent Machine Learning Pipeline
- **Dual-Model Inference:** The system dynamically trains two distinct `RandomForest` classifiers using the Django ORM natively via Pandas.
  - **Personalized Mode:** Inference drawn strictly from your individual habits traversing your own history nodes.
  - **Global Mode:** A collective model trained collaboratively on all system users' anonymized entries.
- **Asynchronous Training:** Submitting a form dispatches a silent background thread to instantly re-train the models on the freshest dataset.

### 🌍 Passive Context Harvesting
BehavioGraph doesn't just listen to what you say; it listens to your environment:
- **Location & Weather:** Seamlessly taps your browser's Geolocation API to fetch live weather conditions and temperatures via the [Open-Meteo API](https://open-meteo.com/).
- **Device & OS:** Automatically extracts and hashes your specific Operating System, Browser engine, and Device dimensions into the analytical pipeline.

### 🏎️ Blazing Fast Frontend (No SPA required)
- **HTMX Driven:** All submissions, forms, and results are swapped seamlessly within the DOM. It achieves true Single-Page Application (SPA) speed while operating purely on standard Django backend templates.
- **Micro-Interactions:** Leverages **Alpine.js** for handling lightweight UI state, form loading animations, and dynamic metadata toggles.
- **Chart.js Visualizations:** Review your personalized chronological history through dynamic graphical distributions.

### 🎨 Premium UI/UX
- **Glassmorphism Design:** A meticulously crafted interface featuring frosted glass panels, smooth hover interactions, and floating ambient orbs.
- **Persistent Theme Toggles:** A fully implemented Light/Dark mode switch bound seamlessly to your browser's `localStorage`.

---

## 🚀 Quick Start

### 1. Requirements
- Python 3.10+
- Environment packages: `django`, `scikit-learn`, `xgboost`, `pandas`, `numpy`

### 2. Installation
Clone the repository and initialize your environment:
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Database initialization
```bash
# Apply Django migrations
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the Engine
```bash
# Start the development server
python manage.py runserver
```
Navigate to `http://127.0.0.1:8000`, register for a new account, and begin building your behavioral dataset!

---

## 📂 Project Architecture

```
prediction-app/
│
├── app/                        # Main Django App
│   ├── models.py               # Database schemas (UserInput, Auth integration)
│   ├── views.py                # Core Python logic and HTMX endpoints
│   ├── forms.py                # Django ModelForms w/ Hidden Alpine metadata vectors
│   ├── ml_pipeline.py          # The core Pandas/Scikit-Learn async trainer
│   └── ml_models/              # Directory holding real-time serialized .pkl models
│
├── static/
│   └── style.css               # Centralized Glassmorphism and UI definitions
│
├── templates/
│   ├── base.html               # Master layout containing Alpine & Nav logic
│   ├── index.html              # The Prediction engine and Global/Personal ML toggles
│   ├── history.html            # The Chart.js historical dashboard
│   └── registration/           # Authentication endpoints (login, register)
│
└── prediction_project/         # Django Core Configuration
```

---

## 📄 License
This project is open-source and licensed under the MIT License.

*Initiated & developed by mbubula6 (2026)*