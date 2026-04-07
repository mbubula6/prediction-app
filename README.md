# 🧠 Behavioral Prediction Web App (Django + ML)

## 📌 Project Overview

This project is a web-based application built with **Django** that collects user input and contextual metadata to generate behavioral predictions using multiple machine learning models.

The goal of the application is to analyze user-provided information along with environmental and device-based metadata to predict:

- The user's current motivational state
- Suggested future actions
- How the user might fill out the form one hour later
- Potential behavioral trends

---

## 🚀 How It Works

### 1️⃣ User Input (Frontend Form)

When a user visits the site, they are presented with a form that collects:

- Name
- Gender
- Preferences (to be extended later)
- Questions such as:
  - What do you want to do right now?
  - What were you doing before entering this site?
  - What were you doing 3 hours ago?
  - Did you sleep well today?

---

### 2️⃣ Automatic Metadata Collection

In addition to manual input, the system collects contextual metadata:

- Current date
- Current time
- Season / part of the year
- Weather (optional – via weather API)
- Temperature
- User location (optional, if enabled)
- Device type (phone / tablet / laptop / desktop)
- Browser and OS (optional)

---

### 3️⃣ Backend Processing

All collected data is sent to the Django backend, where it is:

1. Cleaned and preprocessed
2. Transformed into model-ready features
3. Sent to the selected machine learning model

---

### 4️⃣ Model Selection

Users can choose which model to use for prediction:

- 🌲 Random Forest (RF)
- 📈 Logistic Regression (LR)
- 🧠 Classical Classifier (CL)
- ⚡ XGBoost

All models are trained beforehand and stored for inference.

---

### 5️⃣ Prediction Output

After form submission, the user receives:

- 🔮 A behavioral prediction
- 💬 A generated text response
- ⏳ A forecast of how they might fill out the form one hour later
- 🎯 Suggested motivational direction

---

## 🏗️ Tech Stack

- **Backend:** Django
- **Frontend:** Django Templates / HTML / CSS / JS
- **Machine Learning:** scikit-learn, XGBoost
- **Database:** SQLite / PostgreSQL (configurable)
- **Optional APIs:** Weather API

---
## 📂 Project Structure

```
project/
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── ml_models/
│   │   ├── random_forest.pkl
│   │   ├── logistic_regression.pkl
│   │   ├── classifier.pkl
│   │   └── xgboost.pkl
│
├── templates/
├── static/
├── manage.py
└── README.md
```
---

## 🧪 Model Training (Concept)

Models are trained using:

- User input history
- Time-based features
- Weather and seasonal data
- Device behavior patterns

Future improvements may include:

- Continuous learning
- User-specific personalization
- Deep learning models
- NLP-based input processing

---

## 🔮 Future Improvements

- Authentication system
- User history dashboard
- Visualization of predictions over time
- Real-time retraining pipeline
- Advanced feature engineering
- Mood or productivity tracking

## 📊 Project Vision

This project explores the intersection of:

- Behavioral prediction
- Context-aware systems
- Machine learning model comparison
- Human motivation modeling

It serves both as:

- A machine learning experimentation platform
- A behavioral analytics prototype

---

## 📄 License

MIT License

---

## 👨‍💻 Author

mbubula6 
2026