# 📰 Fake News Detection using BERT + Real-Time News Verification

A Fake News Detection Web App built using BERT, FastAPI, Streamlit, SQLite, and Real-Time News APIs.

This system not only detects fake news using BERT, but also verifies news in real-time using:

* NewsAPI
* GNews API



The system combines:

* Machine Learning (BERT)
* Real-Time News Verification
* Multi-API Integration
* Interactive UI

This makes the project **accurate, scalable, and production-ready**.

---


# Features

✅ Fake News Detection using BERT
✅ Real-Time News Verification
✅ Global News Coverage
✅ Multi-API Support (NewsAPI + GNews)
✅ Confidence Score Prediction
✅ User Authentication (Signup/Login)
✅ Professional UI (Streamlit + HTML + CSS)
✅ FastAPI (Backend)
✅ SQLite Database
✅ Secure API Key Handling (.env)


---

#  How It Works

1. User Authentication
Users first create an account using Signup and then Login securely using SQLite database authentication.
2. User Input
After login, users enter a news headline or article in the prediction page.
3. Frontend Request
The Streamlit UI sends the news text to the FastAPI backend using a POST request.
4. BERT Model Prediction
The backend processes the text using a trained BERT model to classify the news as REAL or FAKE.
5. Confidence Score Calculation
The system calculates prediction confidence using softmax probabilities.
6. Real-Time News Verification
The system verifies the news using trusted sources:
* NewsAPI
* GNews API
7. Final Response
The backend returns:
* Prediction (REAL / FAKE)
* Confidence Score
* Verification Status
8. Result Display
The Streamlit UI displays the result:
* REAL News
* FAKE News

---

# 🛠️ Technologies Used

* Python
* BERT (Transformers)
* SQLite
* FastAPI
* Streamlit
* HTML
* CSS
* NewsAPI
* GNews API
* Pandas
* Scikit-learn
* python-dotenv

---






# 📂 Project Structure(how i created project)-----------------------------

fake-news-detecter/
│
├── app.py
├── ui.py
├── auth.py
├── fake_news_bert/ (files will be generated after training model by running file train_model.py)
├── train_model.py
├── prepare_data.py
├── Fake.csv (downloaded from kaggle)
├── True.csv  (downloaded from kaggle)
├── requirements.txt
├── README.md
├── .env (not uploaded in github)
└── .gitignore




# ⚙️ Installation & Setup (Step by Step)

# Step 1 — Clone Repository
git clone https://github.com/mansiyadav1209/fake-news-detector.git
cd fake-news-detector

# Step 2 — Install Requirements
pip install -r requirements.txt

# Step 3 — Create .env file

Create .env file in root folder

NEWS_API_KEY=your_newsapi_key
GNEWS_API_KEY=your_gnews_key

Get API keys:

NewsAPI
https://newsapi.org

GNews
https://gnews.io


and replace your_newsapi_key and your_gnews_key with the NewsAPI and ENews API keys.


(------>to get these api keys you first need to sign up at these links of NewsAPI and GNews and then, it will generate a key for you in both news api gnews api websites<---------------------)


# Step 4 — Add Dataset

Download dataset:

Fake.csv
True.csv

Place both files in project folder:

project/
├── Fake.csv
├── True.csv

# Step 5 — Prepare Dataset

Run:

python prepare_data.py


This will create:

fake_news.csv

# Step 6 — Train Model

Run:

python train_model.py

This will create files inside*******:

fake_news_bert/

as:

fake_news_bert/
│── config.json
│── tokenizer_config.json
│── tokenizer.json
│── model.safetensors

Training time:

CPU → 2–3 hours
GPU → 10–20 minutes

# Step 7 — Run Backend
uvicorn app:app --reload


# Step 8 — Run UI (on new** terminal) :
streamlit run ui.py

Open browser:

http://localhost:8501








# ▶️ Run Project   ------>(commands to run project)

## Start Backend

```
uvicorn app:app --reload
```


---

## Start Frontend (run on **new** terminal****)

```
streamlit run ui.py
```

---

## Open Browser

```
http://localhost:8501
```

---------------------------------------------------------------------------------------------------








# NOW check:



#  Example check news>
Global markets fall as oil prices rise amid Middle East tensions



#  Example Output>

```
Prediction: REAL

Confidence: 91%

Verification: Found in trusted sources
```

---

# 📊 Dataset

The model was trained using Fake and Real News dataset:

* Political News
* Economic News
* Health News
* Science News
* World News

Dataset Sources:

* Kaggle Fake News Dataset
* Custom Dataset

---


# 🤖 Model Details

Model Used:

* BERT (bert-base-uncased)
* Fine-tuned for Binary Classification

Labels:

* 0 → Fake
* 1 → Real

---




# 🏗️ System Architecture

User Signup/Login
        ↓
Streamlit UI
        ↓
FastAPI Backend
        ↓
BERT Model Prediction
        ↓
NewsAPI + GNews Verification
        ↓
Return Result
        ↓
Display Output


---



# 🔮 Future Improvements

* Prediction History
* Multi-language Support
* Deploy on cloud
* Browser extension
* Improve dataset size
* Admin Dashboard

---

# 🎓 Final Year Project

This project was developed as a **Final Year Major Project** demonstrating:

* Machine Learning
* NLP
* API Integration
* Full Stack Development
* Real-time Data Processing

---

# 👨‍💻 Author

Mansi Yadav
Final Year B.Tech Student

---

# ⭐ If you like this project, give it a star!
