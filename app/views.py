from flask import render_template
from app import app
from .request import get_sources,get_articles,get_topHeadLines


#views
@app.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''

  news_sources = get_sources()
  articles = get_articles()
  topHeadLines = get_topHeadLines
