# Exchange Rate Application

A Python application that fetches real-time exchange rates from the ExchangeRate-API service.

## Project Structure

```
ExchangeRate/
├── app.py                 # Main application entry point
├── requirements.txt       # Python dependencies
├── LICENSE               # Project license
├── README.md            # This file
├── configs/
│   └── config.py        # Configuration (API key, base URL)
├── services/
│   ├── __init__.py
│   └── exchange_services.py  # Exchange rate service logic
├── tests/
│   ├── test_exchange.py  # Unit tests with mocking
│   └── test_app.py       # Integration tests with real API
└── exchrate/            # Python virtual environment
```

## Setup

### 1. Create Virtual Environment
```bash
python -m venv exchrate
```

### 2. Activate Virtual Environment
**Windows (PowerShell):**
```powershell
.\exchrate\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
exchrate\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source exchrate/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Configuration

### API Key Setup

1. Create a `.env` file in the project root:
```bash
touch .env
```

2. Add your ExchangeRate-API key to `.env`:
```
EXCHANGE_RATE_API_KEY=your_api_key_here
```

3. Get your API key from [ExchangeRate-API](https://www.exchangerate-api.com/) (free tier available)

**Important:** Never commit the `.env` file to version control. Add it to `.gitignore`:
```
.env
.env.local
```

The application loads the API key from the environment variable at runtime, keeping it secure.

## Running the Application

Interactive mode - prompts for currency input:
```bash
python app.py
```

Example:
```
Enter the base currency (e.g., USD): USD
Enter the target currency (e.g., EUR): EUR
Exchange rate from USD to EUR: 0.92
```

## Running Tests

### Unit Tests (with mocking)
Tests with mocked API responses:
```bash
pytest tests/test_exchange.py -v
```

### Integration Tests (real API)
Tests that call the real API:
```bash
pytest tests/test_app.py -v -s
```

Or run directly:
```bash
python tests/test_app.py
```

### Run All Tests
```bash
pytest tests/ -v
```

## API Service

The application uses **ExchangeRate-API** (https://www.exchangerate-api.com/)

### Example API Response:
```json
{
  "result": "success",
  "conversion_rates": {
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 149.50,
    "GHS": 11.80
  }
}
```

## Dependencies

- `requests` - HTTP library for API calls
- `python-dotenv` - Environment variable management
- `pytest` - Testing framework
- `certifi` - SSL certificates
- `charset-normalizer` - Character encoding detection
- `idna` - Internationalized domain names
- `urllib3` - HTTP client

See `requirements.txt` for all dependencies and versions.

## Troubleshooting

### `ModuleNotFoundError: No module named 'services'`
Ensure you're running from the project root directory and the virtual environment is activated.

### `NameError: API key not found`
Check that `configs/config.py` contains a valid API key.

### API Rate Limiting
The free tier of ExchangeRate-API has request limits. If you exceed them, wait before making more requests.

## License

See LICENSE file for details.
