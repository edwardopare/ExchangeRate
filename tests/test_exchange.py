import sys
from pathlib import Path

# Add parent directory to path so imports work
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from unittest.mock import patch
from services.exchange_services import ExchangeRate


@patch('services.exchange_services.requests.get')
def test_get_exchange_rate(mock_get):
    
    #mock api response
    mock_get.return_value.json.return_value = {
        "result": "success",
        "conversion_rates": {
            "GHS": 11.80
        }
    }
    
    
    service = ExchangeRate()
    rate = service.get_rate("USD", "GHS")
    
    assert rate == 11.80