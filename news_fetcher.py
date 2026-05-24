import requests

def get_news():
    url = "https://newsapi.org/v2/everything?q=stock%20market&apiKey=0f856775263c47368cc682ceab22e1c7"
    response = requests.get(url).json()

    articles = response.get("articles", [])[:3]

    news_text = ""

    for a in articles:
        news_text += f"{a['title']} - {a['description']}\n\n"

    return news_text