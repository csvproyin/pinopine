import yfinance as yf
from ta.momentum import RSIIndicator


def get_signal(stock):

    try:

        data = yf.download(
            stock + ".NS",
            period="3mo",
            interval="1d"
        )

        if data.empty:
            return "❌ Stock not found."

        close_prices = data["Close"].squeeze()

        rsi = RSIIndicator(close_prices).rsi()

        latest_rsi = round(rsi.iloc[-1], 2)

        latest_price = round(close_prices.iloc[-1], 2)

        if latest_rsi < 30:
            signal = "🟢 BUY"

        elif latest_rsi > 70:
            signal = "🔴 SELL"

        else:
            signal = "⚠️ HOLD"

        return f"""
📊 {stock.upper()} SIGNAL

💰 Price: ₹{latest_price}

📈 RSI: {latest_rsi}

🚦 Signal: {signal}

🤖 AI Insight:
RSI below 30 may indicate oversold conditions.
RSI above 70 may indicate overbought conditions.
"""

    except Exception as e:

        return f"❌ Error: {e}"