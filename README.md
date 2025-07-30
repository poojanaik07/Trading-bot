Binance Futures Trading Bot

A simple Python trading bot for Binance Futures Testnet. It allows you to place market, limit, and stop-market orders via a command-line interface (CLI). The bot logs all API requests, responses, and errors.

Features:
Market, limit, and stop-market orders
Logging of API requests and errors
Easy-to-use CLI interface

How to Run:
Clone the repo:
git clone https://github.com/poojanaik07/Trading-bot
cd trading-bot

Create and activate a virtual environment:
python -m venv venv

Install dependencies:
pip install -r requirements.txt

Set your Binance API keys:
How to Set API Keys:
Create a Binance Testnet account at Binance Testnet.
Get your API key and secret.
Set your API_KEY and API_SECRET as environment variables or directly in the code.


✅ Step-by-step Inputs with Example:
1. 🔹 Enter symbol (e.g., BTCUSDT):
Meaning: The trading pair.

Valid examples:

BTCUSDT

ETHUSDT

BNBUSDT

⚠️ Make sure the pair is available in Binance Futures Testnet.

2. 🔹 Enter side (BUY or SELL):
Meaning: Whether you want to go long (BUY) or short (SELL).

Valid options:

BUY

SELL

3. 🔹 Enter order type:
Meaning: The type of order you want to place.

Valid options:

MARKET – executes immediately at market price

LIMIT – executes at a specific price you enter

STOP_MARKET – triggers a market order once price hits your stop

4. 🔹 Enter quantity:
Meaning: The amount of asset (like BTC or ETH) to buy/sell.

Example:

0.001 (for BTC)

0.01 (for ETH)

⚠️ Be sure your quantity meets Binance Futures minimum size for that symbol.

5. Additional inputs depending on the order type:
If you chose LIMIT:

🔹 Enter limit price: → e.g., 66000.00

If you chose STOP_MARKET:

🔹 Enter stop price: → e.g., 64000.00

🔄 Full Example (for MARKET order):
mathematica
Copy
Edit
🔹 Enter symbol (e.g., BTCUSDT): BTCUSDT
🔹 Enter side (BUY or SELL): BUY
🔹 Enter order type: MARKET
🔹 Enter quantity: 0.001
🔄 Full Example (for LIMIT order):
mathematica
Copy
Edit
🔹 Enter symbol (e.g., BTCUSDT): BTCUSDT
🔹 Enter side (BUY or SELL): SELL
🔹 Enter order type: LIMIT
🔹 Enter quantity: 0.001
🔹 Enter limit price: 67000

Run the bot:
python cli.py
