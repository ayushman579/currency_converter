import streamlit as st
import streamlit as st
from db import init_db, save_conversion, fetch_conversions
import requests

# Initialize the database only once using Streamlit's run-once mechanism
@st.cache_resource
def setup_database():
    init_db()

setup_database()

API_KEY = "df04799ba8f2719084b6096d"
API_BASE_URL = "https://v6.exchangerate-api.com/v6"

def get_exchange_rate(base_currency, target_currency, amount):
    url = f"{API_BASE_URL}/{API_KEY}/pair/{base_currency.upper()}/{target_currency.upper()}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get("result") == "success":
            rate = data["conversion_rate"]
            return round(rate * amount, 4)
        else:
            st.error("API error: " + str(data))
            return None
    except Exception as e:
        st.error(f"Error fetching exchange rate: {e}")
        return None

# Streamlit UI
st.title("💱 Currency Converter")

base = st.text_input("From Currency (e.g. USD)", "USD")
target = st.text_input("To Currency (e.g. EUR)", "EUR")
amount = st.number_input("Amount to Convert", min_value=0.0, value=100.0)

if st.button("Convert"):
    result = get_exchange_rate(base, target, amount)
    if result is not None:
        st.success(f"{amount} {base.upper()} = {result} {target.upper()}")
