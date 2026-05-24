from flask import Flask
from threading import Thread
import os
from portfolio import portfolio, save_portfolio
from watchlist import watchlist, save_watchlist
from alerts_data import alerts, save_alerts
from live_price import get_stock_price
from trading_signal import get_signal
from chart_generator import generate_chart
from telegram_bot import send_photo
from losers import get_losers
from gainers import get_gainers
from ai_engine import analyze
from news_fetcher import get_news
from telegram_bot import send_message, get_updates
from live_price import get_stock_price

import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

print("=" * 40)
print("🤖 AI MARKET BOT IS LIVE")
print("📡 Waiting for Telegram commands...")
print("=" * 40)

updates = get_updates()

if updates["result"]:
    last_update_id = updates["result"][-1]["update_id"]
else:
    last_update_id = 0

send_message("🤖 AI Market Assistant is now LIVE!")
morning_news = get_news()
morning_result = analyze(morning_news)
send_message("🌅 DAILY MARKET UPDATE\n\n" + morning_result)

Thread(target=run_web).start()

while True:
    updates = get_updates()

    for alert in alerts:

        try:

            stock = alert["stock"]
            target = alert["target"]

            result = get_stock_price(stock)

            price_text = result.split("₹")[1]

            current_price = float(price_text)

            if current_price >= target:

                send_message(
                    f"🚨 PRICE ALERT\n\n"
                    f"{stock.upper()} crossed ₹{target}\n\n"
                    f"💰 Current Price: ₹{current_price}"
                )

                alerts.remove(alert)
        except:
            pass

    for u in updates["result"]:

        try:
            update_id = u["update_id"]
            if update_id <= last_update_id:
                continue
            last_update_id = update_id
            text = u["message"]["text"].lower()

            # NEWS
            if text == "/news":
                send_message("📡 Fetching latest market news...")
                news = get_news()
                result = analyze(news)
                send_message("📊 MARKET NEWS UPDATE\n\n" + result)

            # NIFTY
            elif text == "/nifty":
                send_message("📈 Analyzing Nifty...")
                result = analyze(
                    "Give short analysis of Nifty market today."
                )
                send_message("📈 NIFTY ANALYSIS\n\n" + result)

            # BANKNIFTY
            elif text == "/banknifty":
                send_message("🏦 Analyzing BankNifty...")
                result = analyze(
                    "Give short analysis of BankNifty today."
                )
                send_message("🏦 BANKNIFTY ANALYSIS\n\n" + result)

            # BTC
            elif text == "/btc":
                send_message("₿ Checking Bitcoin market...")
                result = analyze(
                    "Give short Bitcoin market sentiment and trend."
                )
                send_message("₿ BITCOIN ANALYSIS\n\n" + result)

            # STOCK
            elif text.startswith("/stock"):
                stock_name = text.replace("/stock", "").strip()

                if stock_name == "":
                    send_message(
                        "❌ Please type a stock name.\nExample: /stock reliance"
                    )

                else:
                    send_message(f"📡 Analyzing {stock_name}...")
                    result = analyze(
                        f"Give short stock analysis, news sentiment, and outlook for {stock_name}."
                    )
                    send_message(
                        f"📈 STOCK ANALYSIS: {stock_name.upper()}\n\n{result}"
                    )

            elif text == "/start":
                send_message(
                    "🤖 Welcome to AI Market Assistant\n\n"
                    "Available Commands:\n\n"
                    "📊 /news - Latest market news\n"
                    "📈 /nifty - Nifty analysis\n"
                    "🏦 /banknifty - BankNifty analysis\n"
                    "₿ /btc - Bitcoin analysis\n"
                    "📉 /stock <name> - Analyze any stock\n\n"
                    "Example:\n"
                    "/stock reliance"
                )
           
            elif text.startswith("/price"):
                stock_name = text.replace("/price", "").strip()

                if stock_name == "":
                    send_message(
                        "❌ Example:\n/price reliance"
                    )

                else:

                    send_message("📡 Fetching live price...")

                    price = get_stock_price(stock_name)

                    send_message(
                        f"📈 {stock_name.upper()} LIVE PRICE\n\n₹{price}"
                    )

            elif text == "/gainers":
                send_message("📊 Checking top gainers...")
                result = get_gainers()
                send_message(result)

            elif text == "/losers":
                send_message("📉 Checking top losers...")
                result = get_losers()
                send_message(result)

            elif text.startswith("/chart"):
                stock_name = text.replace("/chart", "").strip()

                if stock_name == "":
                    send_message(
                "❌ Example:\n/chart reliance"
                )

                else:
                    send_message("📈 Generating stock chart...")
                    chart = generate_chart(stock_name)

                if chart:
                    send_photo(chart)

                else:
                    send_message("❌ Stock not found.")

            elif text.startswith("/signal"):
                stock_name = text.replace("/signal", "").strip()

                if stock_name == "":
                    send_message(
                        "❌ Example:\n/signal reliance"
                    )

                else:
                    send_message("🤖 Generating trading signal...")
                    result = get_signal(stock_name)
                    send_message(result)

            elif text.startswith("/alert"):
                parts = text.split()

                if len(parts) != 3:
                    send_message(
                        "❌ Example:\n/alert reliance 1400"
                    )

                else:

                    stock = parts[1].lower()
                    target = float(parts[2])
                    alerts.append({   
                    "stock": stock,
                    "target": target
                    })
                    save_alerts()

                send_message(
                    f"🚨 Alert set for {stock.upper()} at ₹{target}"
                )

            elif text.startswith("/watch"):
                stock = text.replace("/watch", "").strip()

                if stock == "":
                    send_message(
                        "❌ Example:\n/watch reliance"
                    )

                else:
                    watchlist.append(stock)
                    save_watchlist()
                    send_message(
                        f"⭐ Added {stock.upper()} to watchlist"
                    )

            elif text == "/mywatchlist":

                if len(watchlist) == 0:

                    send_message("📭 Watchlist is empty.")

                else:

                    message = "⭐ YOUR WATCHLIST\n\n"

                    for stock in watchlist:

                        message += f"• {stock.upper()}\n"

                    send_message(message)

            elif text.startswith("/buy"):

                parts = text.split()

                if len(parts) != 3:
                    send_message(
                        "❌ Example:\n/buy reliance 10"
                    )

                else:
                    stock = parts[1].lower()
                    quantity = int(parts[2])

                    if stock in portfolio:
                        portfolio[stock] += quantity
                        save_portfolio()

                    else:
                        portfolio[stock] = quantity
                        save_portfolio()

                    send_message(
                        f"✅ Added {quantity} shares of {stock.upper()}"
                    )   

            elif text == "/portfolio":

                if len(portfolio) == 0:
                    send_message("📭 Portfolio is empty.")

                else:
                    message = "💼 YOUR PORTFOLIO\n\n"
                    total_value = 0

                for stock, quantity in portfolio.items():

                    price = get_stock_price(stock)
                    value = price * quantity
                    total_value += value
                    message += (
                        f"📈 {stock.upper()}\n"
                        f"Shares: {quantity}\n"
                       f"Value: ₹{round(value,2)}\n\n"
                    )
                message += f"💰 Total Portfolio Value: ₹{round(total_value,2)}"
                send_message(message)

            # HELP
            elif text == "/help":

                send_message(
                    "🤖 COMMAND MENU\n\n"
                    "📊 /news - Latest market news\n"
                    "📈 /nifty - Nifty analysis\n"
                    "🏦 /banknifty - BankNifty analysis\n"
                    "₿ /btc - Bitcoin analysis\n"
                    "📉 /stock <name> - Analyze any stock\n"
                    "/price <name>\n"
                    "/gainers\n"
                    "/losers\n"
                    "/chart <name>\n"
                    "/signal <name>\n"
                    "/alert <stock> <price>\n"
                    "/buy <stock> <qty>\n"
                    "/portfolio"
                )

        except Exception as e:
            print("⚠️ Error:", e)

    time.sleep(5)