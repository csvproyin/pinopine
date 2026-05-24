import schedule
import time

from telegram_bot import send_message
from market_news import get_market_news


def morning_update():

    news = get_market_news()

    message = (
        "📈 GOOD MORNING TRADERS\n\n"
        "📰 MARKET NEWS\n\n"
        f"{news}"
    )

    send_message(message)


schedule.every().day.at("09:00").do(morning_update)


def run_scheduler():

    while True:

        schedule.run_pending()

        time.sleep(30)