import yfinance as yf

def get_stock_price(stock):

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

    price = round(data.info["currentPrice"], 2)

    return price