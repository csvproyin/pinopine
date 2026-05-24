import yfinance as yf

def get_gainers():

    stocks = {
        "RELIANCE": "RELIANCE.NS",
        "TCS": "TCS.NS",
        "INFY": "INFY.NS",
        "HDFCBANK": "HDFCBANK.NS",
        "ICICIBANK": "ICICIBANK.NS"
    }

    results = []

    for name, symbol in stocks.items():

        try:

            data = yf.Ticker(symbol)

            hist = data.history(period="2d")

            old_price = hist["Close"].iloc[-2]
            new_price = hist["Close"].iloc[-1]

            percent = ((new_price - old_price) / old_price) * 100

            results.append((name, round(percent, 2)))

        except:
            pass

    results.sort(key=lambda x: x[1], reverse=True)

    message = "📈 TOP GAINERS\n\n"

    for i, stock in enumerate(results[:5], start=1):

        message += f"{i}. {stock[0]}  {stock[1]}%\n"

    return message