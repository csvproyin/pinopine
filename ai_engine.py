from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def analyze(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
    {
        "role": "system",
        "content": """You are a professional stock market analyst.

        Summarize the news in this format:

        📊 Market Summary:
        - 3–5 bullet points (very short)

        📈 Impact:
        - What it means for market (bullish/bearish/neutral)

        🔥 Key Stocks:
        - Mention important stocks/sectors affected

        Keep it SHORT, clear, and powerful."""
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content