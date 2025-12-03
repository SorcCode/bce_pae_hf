import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# -------------------------------------
# 1. Get S&P 100 constituents
# -------------------------------------

tickers = [
    "AAPL", "ABT", "ADBE", "AIG", "AMD", "AMGN", "AMT", "AMZN",
    "AXP", "BA", "BAC", "BK", "BKNG", "BLK", "BMY", "BRK.B", "C",
    "CAT", "CL", "CMCSA", "COF", "COP", "COST", "CSCO", "CVS", "CVX",
    "DE", "DHR", "DIS", "DUK", "EMR", "FDX", "GD", "GE", "GILD",
    "GS", "HD", "HON", "IBM", "INTC", "INTU", "JNJ",
    "JPM", "KO", "LIN", "LLY", "LMT", "LOW", "MA", "MCD", "MDT",
    "MMM", "MO", "MRK", "MS", "MSFT", "NEE", "NKE",
    "NVDA", "ORCL", "PEP", "PFE", "PG", "QCOM",
    "RTX", "SBUX", "SCHW", "SO", "SPG", "T", "TGT", "TMO",
    "TXN", "UNH", "UNP", "UPS", "USB", "VZ", "WFC", "WMT", "XOM"
]
# Ensure tickers are in Yahoo Finance format
tickers = [t.replace('.', '-') for t in tickers]

print(f"Found {len(tickers)} tickers:")
print(tickers)

# -------------------------------------
# 2. Define date range (last 25 years)
# -------------------------------------
end_date = datetime.today()
start_date = end_date - timedelta(days=25 * 365)

# -------------------------------------
# 3. Download S&P 100 index (^OEX)
# -------------------------------------
oex_close = yf.download(
    "^OEX",
    start="2000-01-01",
    end=end_date.strftime("%Y-%m-%d")
)["Close"]

print("\nS&P 100 Index Close:")
print(oex_close.head())

# -------------------------------------
# 4. Download close prices for all S&P 100 members
# -------------------------------------
data = yf.download(
    tickers,
    start="2000-01-01",
    end=end_date.strftime("%Y-%m-%d")
)["Close"]

print("\nMember Close Prices:")
print(data.head())
data.to_csv('closing_prices.csv')

print(f"{len(tickers)} db részvény maradt benne")
