import requests
API_KEY = "df04799ba8f2719084b6096d"  # Replace with your real key
API_BASE_URL = "https://v6.exchangerate-api.com/v6"

def get_exchange_rate(base_currency: str, target_currency: str, amount: float = 1.0) -> float:
    url = f"{API_BASE_URL}/{API_KEY}/pair/{base_currency.upper()}/{target_currency.upper()}"
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        print("DEBUG: API response:", data)

        if data.get("result") == "success":
            rate = data.get("conversion_rate")
            return round(rate * amount, 4)
        else:
            print("ERROR: API response unsuccessful:", data)
            return None
    except Exception as e:
        print(f"API Error: {e}")
        return None


