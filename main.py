from ai_engine import analyze
from news_fetcher import get_news
from telegram_bot import send_message

news = get_news()

result = analyze(news)

print(result)

send_message(result)