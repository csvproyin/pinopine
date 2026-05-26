import yfinance as yf

STOCKS = {
    "RELIANCE": "RELIANCE.NS", "TCS": "TCS.NS", "INFY": "INFY.NS",
    "HDFCBANK": "HDFCBANK.NS", "ICICIBANK": "ICICIBANK.NS",
    "SBIN": "SBIN.NS", "AXISBANK": "AXISBANK.NS", "ITC": "ITC.NS",
    "WIPRO": "WIPRO.NS", "TATAMOTORS": "TATAMOTORS.NS",
    "MARUTI": "MARUTI.NS", "SUNPHARMA": "SUNPHARMA.NS",
    "TATASTEEL": "TATASTEEL.NS", "BHARTIARTL": "BHARTIARTL.NS",
    "LT": "LT.NS"
}

def get_losers():
    results = []
    for name, symbol in STOCKS.items():
        try:
            hist = yf.Ticker(symbol).history(period="2d")
            old = hist["Close"].iloc[-2]
            new = hist["Close"].iloc[-1]
            percent = round(((new - old) / old) * 100, 2)
            results.append((name, percent))
        except:
            pass

    results.sort(key=lambda x: x[1])
    message = "📉 TOP LOSERS TODAY\n\n"
    for i, (stock, change) in enumerate(results[:5], start=1):
        message += f"{i}. 🔴 {stock}  {change}%\n"
    return message