# import streamlit as st
# import requests

# # Page config
# st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")

# # Title
# st.markdown("<h1 style='text-align: center;'>📰 Fake News Detector</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align: center;'>Powered by BERT + FastAPI</p>", unsafe_allow_html=True)

# # Input box
# text = st.text_area("Enter News Text Below:", height=150)

# # Predict button
# if st.button("🔍 Predict"):
#     if text.strip() == "":
#         st.warning("Please enter some text!")
#     else:
#         try:
#             response = requests.post(
#                 "http://127.0.0.1:8000/predict",
#                 json={"text": text}
#             )

#             result = response.json()
#             prediction = result["prediction"]
#             confidence = result["confidence"]

#             # Display result with styling
#             if prediction == "REAL":
#                 st.success(f"✅ Prediction: {prediction}")
#             else:
#                 st.error(f"❌ Prediction: {prediction}")

#             st.info(f"Confidence Score: {confidence:.2f}")

#         except:
#             st.error("⚠️ Backend not running! Please start FastAPI server.")

# # Divider
# st.markdown("---")

# # History section (session-based)
# if "history" not in st.session_state:
#     st.session_state.history = []

# if st.button("📜 Save Last Result"):
#     if text:
#         st.session_state.history.append(text)

# # Show history
# if st.session_state.history:
#     st.subheader("📌 Previous Inputs")
#     for i, item in enumerate(st.session_state.history[-5:], 1):
#         st.write(f"{i}. {item}")

import streamlit as st
import requests

st.title("📰 Fake News Detector (AI + Real-Time Verification)")

news = st.text_area("Enter News")

if st.button("Check News"):
    
    if news.strip() == "":
        st.warning("Please enter news text")
    
    else:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json={"text": news}
        )

        result = response.json()

        st.subheader("Prediction")
        
        if result["prediction"] == "REAL":
            st.success(f"REAL ✅")
        else:
            st.error(f"FAKE ❌")

        st.write(f"Confidence: {result['confidence']}%")
        st.write(f"Verification: {result['verification']}")