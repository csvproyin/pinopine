import yfinance as yf
import mplfinance as mpf

def generate_chart(stock):

    stock_map = {
        "reliance": "RELIANCE.NS",
        "tcs": "TCS.NS",
        "infosys": "INFY.NS",
        "hdfcbank": "HDFCBANK.NS"
    }

    symbol = stock_map.get(stock.lower())

    if not symbol:
        return None

    data = yf.Ticker(symbol)

    hist = data.history(period="1mo")

    filename = f"{stock}_candles.png"

    mpf.plot(
        hist,
        type="candle",
        style="charles",
        title=f"{stock.upper()} Candlestick Chart",
        volume=True,
        savefig=filename
    )

    return filename