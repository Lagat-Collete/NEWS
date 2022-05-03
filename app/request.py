from app import app
import urllib.request,json
from .models import *


#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config['NEWS_API_BASE_URL']

def get_sources():
    '''
    Function that gets the json response to our url request
    '''

    get_sources_url = base_url.format( api_key)

    with urllib.request.urlopen(get_sources_url) as url:
      get_sources_data = url.read()
      get_sources_response = json.loads(get_sources_data)
      

      source_results = None

      if get_sources_response['results']:
         source_results_list = get_sources_response['results']
         source_results = process_source_results(source_results_list)
   
    return source_results


def process_source_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects
   
    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
       id = source_item.get('id')
       name = source_item.get('name')
       description = source_item.get('description')
       url = source_item.get('url')
       category = source_item.get('category')
       language = source_item.get('language')
       country = source_item.get('country')

    source_object = source(id,name,description, url, category, language, country)
    source_results.append(source_object)
    return source_results

def get_topHeadlines():
    get_topHeadlines_url = headlines_url.format(api_key)

    with urllib.request.urlopen(get_topHeadlines_url) as url :
      topHeadlines_data = url.read()
      topHeadlines_response = json.loads(topHeadlines_data)

      topHeadlines_results = None

      if topHeadlines_response['results']:
        topHeadlines_results_list = topHeadlines_response['articles']
        topHeadlines_results = process_topHeadlines_results(topHeadlines_results_list)
        
        return(topHeadlines_results)

def process_topHeadlines_results(topHeadlines_results_list):
  '''
  process top headlines results and transform them to a list of objects
  '''
  topHeadlines_results = []
  for topHeadlines_item in topHeadlines_results_list :

    id = topHeadlines_item.get('id')
    name = topHeadlines_item.get('name')
    author = topHeadlines_item.get('author')
    title = topHeadlines_item.get('title')
    description = topHeadlines_item.get('description')
    url = topHeadlines_item.get('url')
    urlToImage = topHeadlines_item.get('urlToImage')
    publishedAt = topHeadlines_item.get('publishedAt')
    content = topHeadlines_item.get('content')

    topHeadlines_object = TopHeadlines(id, name, author, title, description, url, urlToImage, publishedAt, content)
    topHeadlines_results.append(topHeadlines_object)
     
    return topHeadlines_results


def get_articles():
    get_articles_url = articles_url.format(api_key)

    with urllib.request.urlopen(get_articles_url) as url :
      articles_data = url.read()
      articles_response = json.loads(articles_data)

      articles_results = None

      if articles_response['results']:
        articles_results_list = articles_response['articles']
        articles_results = process_articles_results(articles_results_list)
        
        return(articles_results)

def process_articles_results(articles_results_list):
  '''
  process top articles results and transform them to a list of objects
  '''
  articles_results = []
  for articles_item in articles_results_list :

    source = articles_item.get('source')
    author = articles_item.get('author')
    title = articles_item.get('title')
    description = articles_item.get('description')
    url = articles_item.get('url')
    urlToImage = articles_item.get('urlToImage')
    publishedAt = articles_item.get('publishedAt')
    content = articles_item.get('content')

    topHeadlines_object = Articles(source, author, title, description, url, urlToImage, publishedAt, content)
    articles_results.append(articles_object)
     
    return articles_results

    
