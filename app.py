from services.exchange_services import ExchangeRate

def main():
    exchange_rate = ExchangeRate()
    
    from_currency = input("Enter the base currency (e.g., USD): ")
    to_currency = input("Enter the target currency (e.g., EUR): ")
    
    try:
        rate = exchange_rate.get_rate(from_currency, to_currency)
        print(f"Exchange rate from {from_currency} to {to_currency}: {rate}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()