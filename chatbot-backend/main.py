from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from bs4 import BeautifulSoup
import requests
import os
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker

app = FastAPI()

app.mount("/static", StaticFiles(directory="."), name="static")

templates = Jinja2Templates(directory="templates")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://<postgres username>:<enter your postgres password>@localhost:5432/",
)

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    text = Column(Text)

Base.metadata.create_all(bind=engine)

def save_article(url: str, text: str):
    article = Article(url=url, text=text)
    session = Session()
    session.add(article)
    session.commit()
    session.close()

def search_articles(query: str):
    session = Session()
    results = session.query(Article).filter(Article.text.ilike(f"%{query}%")).all()
    session.close()
    return results

@app.post('/scrape')
async def scrape_article(request: Request):
    data = await request.json()
    url = data['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    article_text = ''
    for p in soup.find_all('p'):
        article_text += p.text + '\n'
    save_article(url, article_text)
    return PlainTextResponse(content=article_text)

@app.get('/search')
async def search(request: Request, q: str):
    results = search_articles(q)

     # Return a list of search results as a JSON response
    return [{'id': result.id} for result in results]

    # return templates.TemplateResponse('results.html', {'request': request, 'results': results})
