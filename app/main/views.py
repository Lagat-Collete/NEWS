
from unicodedata import category
from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_sources,search_article, get_articles, get_topHeadlines, get_sourceHeadlines

#Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Obtaining News sources
    science = get_sources("science")
    health = get_sources('health')
    business = get_sources('business')
    technology = get_sources('technology')
    entertainment = get_sources('entertainment')
    sports = get_sources('sports')
    title = 'Home - Welcome to The best News Website Online'

    search_article =request.args.get('search_query')
    if search_article:
        return redirect(url_for('search', articles_name = search_article))
    else:
        return render_template('index.html', title= title, business = business , technology= technology, entertainment = entertainment, sports = sports, science = science, health = health)

@main.route('/source_articles/<id>')
def articles(id):
    '''
    View root page function that returns the index page and its data
    '''

    #news sources
    source_articles = get_articles(id)
    return render_template('source.html',title = 'this is source', source_articles = source_articles)


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
    