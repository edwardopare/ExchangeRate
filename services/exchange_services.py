import requests
from configs.config import BASE_URL 


class ExchangeRate:
    
    def get_rate(self, from_currency, to_currency):
        
        """ fetching exchange rate from API """
        url = f"{BASE_URL}/latest/{from_currency}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data["result"] != "success":
                raise Exception("API request failed")
            
            rate = data["conversion_rates"].get(to_currency)
            
            if not rate:
                raise Exception(f"No rate found for {to_currency}")
            return rate 
        
        except requests.exceptions.RequestException as e:
            raise Exception(f"Connection error: {e}")
            
        
        