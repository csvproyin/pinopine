import openai
from openai import OpenAI

client = OpenAI()


def get_market_news():

    headlines = [
        "RBI signals economic optimism",
        "IT stocks rally amid AI boom",
        "Global markets remain positive",
        "Banking sector sees strong buying"
    ]

    prompt = f"""
    Analyze these market headlines and provide:

    1. Overall market sentiment
    2. Key factors
    3. Short AI outlook

    Headlines:
    {headlines}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content