import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from services.exchange_services import ExchangeRate

from services.exchange_services import ExchangeRate

def test_real_api_exchange_rate():
    """Test real API call to exchange rate service"""
    service = ExchangeRate()
    
    # Test with real API
    rate = service.get_rate("USD", "GHS")
    
    # Verify we got a valid rate
    assert isinstance(rate, (int, float))
    assert rate > 0
    print(f"Exchange rate USD to GHS: {rate}")

def test_real_api_multiple_currencies():
    """Test real API with multiple currency pairs"""
    service = ExchangeRate()
    
    test_pairs = [
        ("USD", "EUR"),
        ("USD", "GBP"),
        ("USD", "JPY"),
        ("EUR", "USD")
    ]
    
    for from_curr, to_curr in test_pairs:
        rate = service.get_rate(from_curr, to_curr)
        assert isinstance(rate, (int, float))
        assert rate > 0
        print(f"{from_curr} to {to_curr}: {rate}")
        

if __name__ == "__main__":
    test_real_api_exchange_rate()
    test_real_api_multiple_currencies()