import yfinance as yf
import pandas as pd

def get_signal(stock):

    stock_map = {
        "reliance": "RELIANCE.NS",
        "tcs": "TCS.NS",
        "infosys": "INFY.NS",
        "hdfcbank": "HDFCBANK.NS"
    }

    symbol = stock_map.get(stock.lower())

    if not symbol:
        return "❌ Stock not found."

    data = yf.Ticker(symbol)

    hist = data.history(period="1mo")

    close = hist["Close"]

    sma_5 = close.tail(5).mean()
    sma_20 = close.tail(20).mean()

    latest_price = round(close.iloc[-1], 2)

    if sma_5 > sma_20:

        signal = "🟢 BUY SIGNAL"
        trend = "Bullish"

    else:

        signal = "🔴 SELL SIGNAL"
        trend = "Bearish"

    result = (
        f"{signal}: {stock.upper()}\n\n"
        f"💰 Current Price: ₹{latest_price}\n"
        f"📈 Trend: {trend}\n"
        f"⚡ SMA 5: {round(sma_5,2)}\n"
        f"📊 SMA 20: {round(sma_20,2)}"
    )

    return result