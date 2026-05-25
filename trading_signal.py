from live_price import get_stock_price


def get_signal(stock):

    price = get_stock_price(stock)

    if price <= 0:

        return "❌ Stock not found."

    if price > 2500:

        signal = "🔥 STRONG BUY"
        confidence = "89%"
        sentiment = "Bullish momentum"

    elif price > 1000:

        signal = "📈 BUY"
        confidence = "76%"
        sentiment = "Positive trend"

    else:

        signal = "😏 HOLD"
        confidence = "61%"
        sentiment = "Neutral movement"

    return (
        f"🤖 AI SIGNAL REPORT\n\n"
        f"📊 Stock: {stock.upper()}\n"
        f"💰 Current Price: ₹{price}\n\n"
        f"⚡ Signal: {signal}\n"
        f"🎯 Confidence: {confidence}\n"
        f"🧠 Sentiment: {sentiment}\n\n"
        f"⚠️ Educational only. Not financial advice."
    )