import requests
import os
from textblob import TextBlob

NEWS_API_KEY = os.getenv("NEWS_API_KEY", "d7644de59e05459ba0c5401ecea1800f")
MEDIASTACK_API_KEY = os.getenv("MEDIASTACK_API_KEY", "eb318a29917dbcc139af022c670a09e2")
GNEWS_API_KEY = os.getenv("GNEWS_API_KEY", "9e6a18445fd7ba49e885486a836dc0f9")


def get_news_from_newsapi(keyword):
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("status") == "ok":
        return [
            {
                "judul": article["title"],
                "sumber": article["source"]["name"],
                "url": article["url"],
                "tanggal": article["publishedAt"],
                "isi": article["description"] or "",
            }
            for article in data.get("articles", [])
        ]
    return []


def get_news_from_mediastack(keyword):
    url = f"http://api.mediastack.com/v1/news?access_key={MEDIASTACK_API_KEY}&keywords={keyword}"
    response = requests.get(url)
    data = response.json()

    if "data" in data:
        return [
            {
                "judul": article["title"],
                "sumber": article["source"],
                "url": article["url"],
                "tanggal": article["published_at"],
                "isi": article["description"] or "",
            }
            for article in data["data"]
        ]
    return []


def get_news_from_gnews(keyword):
    url = f"https://gnews.io/api/v4/search?q={keyword}&token={GNEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if "articles" in data:
        return [
            {
                "judul": article["title"],
                "sumber": article["source"]["name"],
                "url": article["url"],
                "tanggal": article["publishedAt"],
                "isi": article["description"] or "",
            }
            for article in data["articles"]
        ]
    return []


def get_all_news(keyword):
    news = []
    news.extend(get_news_from_newsapi(keyword))
    news.extend(get_news_from_mediastack(keyword))
    news.extend(get_news_from_gnews(keyword))
    return news


def analisis_sentimen(teks):
    analysis = TextBlob(teks)
    score = analysis.sentiment.polarity  # Skor antara -1 (negatif) hingga +1 (positif)

    if score > 0.1:
        return "Positif"
    elif score < -0.1:
        return "Negatif"
    else:
        return "Netral"