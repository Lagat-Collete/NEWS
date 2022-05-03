from flask import render_template
from app import app
from .request import get_sources,get_articles,get_topHeadlines


#views
@app.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''
# Obtaining News sources 
 
  news_sources = get_sources()
  topHeadLines = get_topHeadlines()
  articles = get_articles()
  title = ' Welcome to your News station'
  return render_template('index.html', title = title,source_list= get_sources, get_topHeadlines = topHeadlines, articles = articles)

@app.route('/source')
def source():
  '''
  View root page function that returns the index page and its
  '''
  #obtaining News Sources
  source = request.args.get("name")
  print(source)
  topHeadlines = get_topHeadlines(source)
  print('topHeadlines', topHeadlines)
  return render_template('source.htm',title = 'this is source', source_list = topHeadlines)


@app.route('/search/<article_name>')
def search(article_name):
  '''
  view function to display the search results
  '''
  article_name_list = article_name.split(" ")
  article_name_format = "+".join(article_name_list)
  searched_articles = search_articles(article_name_format)
  title - f'search results for {article_name}'
  return render_template('search.html',articles = searched_articles)