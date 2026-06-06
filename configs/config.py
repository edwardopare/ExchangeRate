import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
if not API_KEY:
    raise ValueError("EXCHANGE_RATE_API_KEY environment variable not set")

BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}"
