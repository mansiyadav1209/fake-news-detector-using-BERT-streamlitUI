# 📰 Real-Time Fake News Detection using BERT

## 📌 Project Overview

This project is an AI-powered **Fake News Detection System** that classifies news as **Real or Fake** using a **BERT-based Machine Learning model** and verifies results using **Real-Time News APIs**.

The system combines:

* Machine Learning (BERT)
* Real-Time News Verification
* Multi-API Integration
* Interactive UI

This makes the project **accurate, scalable, and production-ready**.

---

# 🚀 Features

✅ Fake News Detection using BERT
✅ Real-Time News Verification
✅ Multi-API Support (NewsAPI + GNews)
✅ Confidence Score
✅ FastAPI Backend
✅ Streamlit UI
✅ Global News Coverage
✅ Secure API Key Handling (.env)

---

# 🧠 How It Works

1. User enters news text
2. BERT Model predicts Real / Fake
3. NewsAPI checks real-time news
4. GNews API verifies global news
5. Final result displayed with confidence score

---

# 🛠️ Technologies Used

* Python
* BERT (Transformers)
* PyTorch
* FastAPI
* Streamlit
* NewsAPI
* GNews API
* Pandas
* Scikit-learn
* python-dotenv

---






# 📂 Project Structure(how i created project)-----------------------------

fake-news-detecter/fnd/
│
├── app.py
├── ui.py
├── train_model.py
├── prepare_data.py
├── Fake.csv (downloaded from kaggle)
├── True.csv  (downloaded from kaggle)
├── requirements.txt
├── README.md
├── .env (not uploaded in github)
└── .gitignore



⚙️ Installation & Setup (Step by Step)

# Step 1 — Clone Repository
git clone git clone https://github.com/mansiyadav1209/fake-news-detector
cd fnd

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
│── pytorch_model.bin
│── tokenizer_config.json
│── tokenizer.json
│── vocab.txt
│── model.safetensors

Training time:

CPU → 1–3 hours
GPU → 10–20 minutes

# Step 7 — Run Backend
uvicorn app:app --reload


# Step 8 — Run UI on (new terminal) :
streamlit run ui.py

Open browser:

http://localhost:8501












# 📂 Project Structure(for users who clone project)--------------------------------------------

```
fake-news-detector/fnd/
│
├── app.py
├── ui.py
├── train_model.py
├── prepare_data.py
├── fake_news_bert/     ***
├── Fake.csv (downloaded from kaggle)
├── True.csv (downloaded from kaggle)
├── fake_news.csv     ***  
├── requirements.txt
├── README.md
├── .env (not uploaded in github)
└── .gitignore
```

---

# ⚙️ Installation

## Step 1: Clone Repository

```
git clone https://github.com/mansiyadav1209/fake-news-detector
cd fnd
```

---

## Step 2: Install Requirements

```
pip install -r requirements.txt
```

---

# 🔐 API Setup (Important)

Create a `.env` file in project folder:

```
NEWS_API_KEY=your_newsapi_key
GNEWS_API_KEY=your_gnews_key
```

Get API Keys from:

NewsAPI
https://newsapi.org/

GNews API
https://gnews.io/


and replace your_newsapi_key and your_gnews_key with the NewsAPI and ENews API keys.


(------>to get these api keys you first need to sign up at these links of NewsAPI and GNews and then, it will generate a key for you in both news api gnews api websites<---------------------)

---





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

```
User Input
     ↓
Streamlit UI
     ↓
FastAPI Backend
     ↓
BERT Model
     ↓
Prediction
     ↓
NewsAPI + GNews Verification
     ↓
Final Result
```

---

# 🔮 Future Improvements

* Add multilingual support
* Add image fake detection
* Deploy on cloud
* Browser extension
* Improve dataset size

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

Final Year B.Tech Student
Real-Time Fake News Detection Project

---

# 📜 License

This project is for educational purposes only.
