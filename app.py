# from fastapi import FastAPI
# from pydantic import BaseModel
# import torch
# from transformers import BertTokenizer, BertForSequenceClassification

# app = FastAPI()

# # Load saved model
# model = BertForSequenceClassification.from_pretrained("fake_news_bert")
# tokenizer = BertTokenizer.from_pretrained("fake_news_bert")

# class NewsInput(BaseModel):
#     text: str

# @app.get("/")
# def home():
#     return {"message": "Fake News Detection API"}

# @app.post("/predict")
# def predict(news: NewsInput):
#     inputs = tokenizer(news.text, return_tensors="pt", truncation=True, padding=True)
    
#     outputs = model(**inputs)
#     probs = torch.nn.functional.softmax(outputs.logits, dim=1)
    
#     confidence, pred = torch.max(probs, dim=1)
    
#     label = "REAL" if pred.item() == 1 else "FAKE"
    
#     return {
#         "prediction": label,
#         "confidence": float(confidence.item())
#     }

# from fastapi import FastAPI
# from pydantic import BaseModel
# from transformers import BertTokenizer, BertForSequenceClassification
# import torch
# import requests
# import torch.nn.functional as F

# app = FastAPI()

# # Load model
# model = BertForSequenceClassification.from_pretrained("fake_news_bert")
# tokenizer = BertTokenizer.from_pretrained("fake_news_bert")

# # Request schema
# class News(BaseModel):
#     text: str


# # 🔎 News API Function
# def verify_news_api(text):
#     url = "https://newsapi.org/v2/everything"
    
#     params = {
#         "q": text,
#         "apiKey": "................",  # replace with your key
#         "language": "en",
#         "pageSize": 3
#     }
    
#     response = requests.get(url, params=params)
#     data = response.json()
    
#     if data.get("totalResults", 0) > 0:
#         return "Found in news sources"
#     else:
#         return "Not found in trusted sources"


# @app.post("/predict")
# def predict(news: News):

#     inputs = tokenizer(news.text, return_tensors="pt", truncation=True, padding=True)

#     outputs = model(**inputs)
#     probs = F.softmax(outputs.logits, dim=1)

#     confidence = torch.max(probs).item()
#     prediction = torch.argmax(probs).item()

#     label = "REAL" if prediction == 1 else "FAKE"

#     # verify using API
#     verification = verify_news_api(news.text)

#     return {
#         "prediction": label,
#         "confidence": round(confidence * 100, 2),
#         "verification": verification
#     }
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import BertTokenizer, BertForSequenceClassification
import torch
import requests
import torch.nn.functional as F
from dotenv import load_dotenv
import os

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")

app = FastAPI()

# Load model
model = BertForSequenceClassification.from_pretrained("fake_news_bert")
tokenizer = BertTokenizer.from_pretrained("fake_news_bert")

class News(BaseModel):
    text: str


# NewsAPI verification
def verify_newsapi(text):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": text,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "pageSize": 3
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data.get("totalResults", 0) > 0:
            return True
    except:
        pass

    return False


# GNews verification
def verify_gnews(text):
    url = "https://gnews.io/api/v4/search"
    params = {
        "q": text,
        "token": GNEWS_API_KEY,
        "lang": "en",
        "max": 3
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data.get("totalArticles", 0) > 0:
            return True
    except:
        pass

    return False


def verify_news(text):
    newsapi = verify_newsapi(text)
    gnews = verify_gnews(text)

    if newsapi or gnews:
        return "Found in trusted sources"
    else:
        return "Not found in trusted sources"


@app.post("/predict")
def predict(news: News):

    inputs = tokenizer(news.text, return_tensors="pt", truncation=True, padding=True)

    outputs = model(**inputs)
    probs = F.softmax(outputs.logits, dim=1)

    confidence = torch.max(probs).item()
    prediction = torch.argmax(probs).item()

    label = "REAL" if prediction == 1 else "FAKE"

    verification = verify_news(news.text)

    return {
        "prediction": label,
        "confidence": round(confidence * 100, 2),
        "verification": verification
    }