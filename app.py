from services.exchange_services import ExchangeRate

def main():
    exchange_rate = ExchangeRate()
    
    from_currency = input("Enter the base currency (e.g., USD): ")
    to_currency = input("Enter the target currency (e.g., EUR): ")
    amount = float(input("Enter the amount to convert: "))
    
    try:
        rate = exchange_rate.get_rate(from_currency, to_currency)
        converted_amount = amount * rate
        print(f"Exchange rate from {from_currency} to {to_currency}: {rate}")
        print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()