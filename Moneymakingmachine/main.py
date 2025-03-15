import streamlit as st
import random
import time
import requests

# Custom CSS for light-themed UI
st.markdown(
    """
    <style>
        body {
            background-color: #f0f8ff; /* Light Blue Background */
            color: #333;
            font-family: 'Arial', sans-serif;
        }
        .stApp {
            background-color: #f0f8ff;
        }
        .stButton > button {
            background-color: #f4f4f4;
            color: #333;
            border-radius: 10px;
            padding: 10px 20px;
            border: 1px solid #ddd;
        }
        .stButton > button:hover {
            background-color: #e0e0e0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💰 Money Making Machine")

# Function to create random amount of money
def generate_money():
    return random.randint(1, 1000)

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("⏳ Counting your money...")
    time.sleep(3)
    amount = generate_money()
    st.success(f"🎉 You made ${amount}!")

# Function to get side hustle ideas from a server
def fetch_side_hustle():
    try:
        response = requests.get("https://fastapi-api.vercel.app/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustle"]
        else:
            return "Freelancing"
    except:
        return "Something went wrong!"

st.subheader("💼 Side Hustle Ideas")
if st.button("Generate Hustle"):
    idea = fetch_side_hustle()
    st.success(f"🚀 {idea}")

# Function to get money-related quotes
def fetch_money_quote():
    try:
        response = requests.get("https://fastapi-api.vercel.app/money_quotes")
        if response.status_code == 200:
            quotes = response.json()
            return quotes["money_quote"]
        else:
            return "Money is the root of all evil!"
    except:
        return "Something went wrong!"

st.subheader("📢 Money-Making Motivation")
if st.button("Get Inspired"):
    quote = fetch_money_quote()
    st.info(f"💡 {quote}")
