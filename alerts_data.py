import json
import yfinance as yf


ALERTS_FILE = "alerts.json"


def load_alerts():

    try:

        with open(ALERTS_FILE, "r") as f:
            return json.load(f)

    except:
        return []


def save_alerts(alerts):

    with open(ALERTS_FILE, "w") as f:
        json.dump(alerts, f, indent=4)


def add_alert(stock, target_price):

    alerts = load_alerts()

    alerts.append({
        "stock": stock.upper(),
        "target": float(target_price)
    })

    save_alerts(alerts)


def check_alerts():

    alerts = load_alerts()
    print("LOADED ALERTS:", alerts)  # DEBUG

    triggered = []
    remaining = []

    for alert in alerts:

        stock = alert["stock"]
        target = alert["target"]

        try:

            ticker = stock + ".NS"
            print(f"Fetching price for: {ticker}")  # DEBUG

            data = yf.download(ticker, period="1d", progress=False)
            print(f"Data received: {data}")  # DEBUG

            current_price = round(float(data["Close"].iloc[-1].values[0]), 2)
            print(f"{stock} current price: {current_price}, target: {target}")  # DEBUG

            if current_price >= target:
                triggered.append(
                    f"🚨 PRICE ALERT\n\n📈 {stock} crossed ₹{target}\n\n💰 Current Price: ₹{current_price}"
                )
            else:
                remaining.append(alert)

        except Exception as e:
            print(f"❌ ERROR for {stock}: {e}")  # DEBUG - was silent before!
            remaining.append(alert)

    save_alerts(remaining)
    return triggered
