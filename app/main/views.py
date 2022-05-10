
from unicodedata import category
from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources,search_article, get_articles, get_topHeadlines, get_sourceHeadlines

#Views
@main.route('/')
@main.route('/index/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
  # Obtaining News sources
    news_sources = get_sources()
    articles = get_articles()
    topHeadlines = get_topHeadlines()
    title = 'Home - Welcome to Worldwide News Website'

    search_article = request.args.get('search_query')
    if search_article:
     return redirect(url_for('search', article_name = search_article))
    else:
     return render_template('index.html', title = title, source_list = news_sources, articles = articles, top_headlines = topHeadlines)

@main.route('/source')
def source():
  '''
  View root page function that returns the index page and its data
  '''

# Obtaining News sources
  source = request.args.get("name")
  print("sourceg", source)
  topHeadlines = get_sourceHeadlines(source)
  print('topHeadlines', topHeadlines)
  return render_template('source.html', title = 'this is sourcepage', source_list = topHeadlines)
  


@main.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display the search results
    '''
    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f'search results for {article_name}'
    return render_template('search.html', article = searched_articles)
    