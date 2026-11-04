from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import time

app = FastAPI()

@app.get("/news")
def get_news():
    url = "https://news.ycombinator.com/"

    response = requests.get(url)
     
    soup = BeautifulSoup(response.text, "html.parser")

    title = []

    for item in soup.find_all("span", class_="titleline"):
        title.append(item.text)


    #Pagination Logic
    start = (page - 1) * limit
    end = start + limit

    return {
        "news": title
    }