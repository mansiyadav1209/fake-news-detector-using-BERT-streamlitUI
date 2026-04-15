import streamlit as st
import requests
import auth

auth.create_user_table()


def load_css():
    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(to right, #eef2f3, #dfe9f3);
    }

    .card {
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 6px 20px rgba(0,0,0,0.1);
        margin-top: 20px;
    }

    .title {
        text-align:center;
        font-size:40px;
        font-weight:600;
        color:#1f4e79;
    }

    .subtitle {
        text-align:center;
        font-size:18px;
        color:gray;
    }

    /* Heading color fix */
    h1, h2, h3, h4, h5, h6 {
        color: black !important;
    }

    /* Button */
    .stButton>button {
        background: linear-gradient(to right,#1f77b4,#4facfe);
        color:white;
        border-radius:10px;
        height:3em;
        width:100%;
        border:none;
        font-size:16px;
    }

    .stButton>button:hover {
        transform: scale(1.02);
        transition:0.3s;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(#1f4e79,#4facfe);
    }

    section[data-testid="stSidebar"] * {
        color:white;
    }

    /* Dark Green Success Box */
    .stSuccess {
        background-color: #0f5132 !important;
        color: white !important;
        border-radius: 10px;
        padding: 10px;
        font-weight: bold;
    }

    .stTextInput input {
        border-radius:10px;
    }

    .stTextArea textarea {
        border-radius:10px;
    }

    </style>
    """, unsafe_allow_html=True)


load_css()

# ---------------- SESSION ----------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Home"


st.title("📰 Fake News Detector")

menu = ["Home", "Login", "Signup", "Prediction"]

choice = st.sidebar.selectbox(
    "Menu",
    menu,
    index=menu.index(st.session_state.page)
)

# ---------------- HOME ----------------

if choice == "Home":
    st.session_state.page = "Home"

    st.markdown("""
    <div class="card">
    <div class="title">📰 Fake News Detector</div>
    <br>
    <div class="subtitle">
    Detect Fake News using AI & BERT Model
    </div>
    <br>
    <center>
    <img src="https://cdn-icons-png.flaticon.com/512/2965/2965879.png" width="120">
    </center>
    </div>
    """, unsafe_allow_html=True)


# ---------------- LOGIN ----------------

elif choice == "Login":
    st.session_state.page = "Login"

    st.markdown("""
    <div class="card">
    <h2 style="text-align:center;">🔐 Login</h2>
    </div>
    """, unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        result = auth.login_user(username, password)

        if result:
            st.session_state.logged_in = True
            st.session_state.page = "Prediction"
            st.success("Login Successful")
            st.rerun()

        else:
            st.error("Invalid credentials")


# ---------------- SIGNUP ----------------

elif choice == "Signup":
    st.session_state.page = "Signup"

    st.markdown("""
    <div class="card">
    <h2 style="text-align:center;">📝 Signup</h2>
    </div>
    """, unsafe_allow_html=True)

    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")

    if st.button("Signup"):
        auth.add_user(new_user, new_pass)
        st.success("Account Created Successfully")


# ---------------- PREDICTION ----------------

elif choice == "Prediction":
    st.session_state.page = "Prediction"

    if st.session_state.logged_in:

        st.markdown("""
        <div class="card">
        <h2 style="text-align:center;">🧠 Fake News Prediction</h2>
        </div>
        """, unsafe_allow_html=True)

        news = st.text_area("Enter News")

        if st.button("Predict"):

            try:
                response = requests.post(
                    "http://127.0.0.1:8000/predict",
                    json={"text": news}
                )

                # result = response.json()["prediction"]
                data = response.json()
                result = data["prediction"]
                confidence = data["confidence"]
                verification = data["verification"]

                if result == "REAL":
                    st.markdown(
                        f'<div style="background-color:#14532d;color:white;padding:12px;border-radius:8px;font-weight:bold;">'
                        f'✅ {result} <br> Confidence: {confidence}% <br> {verification}'
                        f'</div>',
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f'<div style="background-color:#7f1d1d;color:white;padding:12px;border-radius:8px;font-weight:bold;">'
                        f'❌ {result} <br> Confidence: {confidence}% <br> {verification}'
                        f'</div>',
                        unsafe_allow_html=True
                    )

                # if result == "REAL":
                #     st.markdown(f'<div style="background-color:#14532d;color:white;padding:12px;border-radius:8px;font-weight:bold;">✅ {result}</div>', unsafe_allow_html=True)
                # else:
                #     st.markdown(f'<div style="background-color:#7f1d1d;color:white;padding:12px;border-radius:8px;font-weight:bold;">❌ {result}</div>', unsafe_allow_html=True)
               

            except:
                st.error("Backend not running")

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.page = "Home"
            st.rerun()

    else:
        st.warning("Please login first")