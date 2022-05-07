
import urllib.request,json
from .models  import Articles, Source, TopHeadlines

#Getting api key
api_key = None
#Getting the base url
base_url = None
#getting headlines url
headlines_url = None
#getting everything url
articles_url = None
#obtaining articles for specific source
source_healine_url = None

def configure_request(app):
  global api_key, base_url, headlines_url, articles_url, source_healine_url
  api_key = app.config['NEWS_HIGHLIGHT_API_KEY']
  base_url = app.config['NEWS_HIGHLIGHT_API_BASE_URL']
  headlines_url = app.config['NEWS_HEADLINES_URL']
  source_healine_url = app.config[' SOURCE_HEADLINE_URL']

def get_sources():
  '''
  Function that gets the json response to our url request
  '''
  print( 'api_key'f'{base_url}{api_key}')
  get_sources_url = base_url.format(api_key)

  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)
    print('results', get_sources_response)

    source_results = None

    if get_sources_response['status']=='ok':
      source_results_list = get_sources_response['sources']
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

     source_object = Source(id, name, description, url, category, language, country)
     source_results.append(source_object)

  return source_results

def get_topHeadlines():
  get_topHeadlines_url = headlines_url.format(api_key)
  print('get_topHeadlines_url',get_topHeadlines_url)

  with urllib.request.urlopen(get_topHeadlines_url) as url:
    topHeadlines_data = url.read()
    topHeadlines_response = json.loads(topHeadlines_data)

    topHeadlines_results = None

    if topHeadlines_response['status'] == 'ok':
      topHeadlines_results_list = topHeadlines_response['articles']
      topHeadlines_results = process_topHeadlines_results(topHeadlines_results_list)

  print('topHeadlines_results', topHeadlines_results)
  return(topHeadlines_results)

def get_sourceHeadlines(source):
  get_sourceHeadlines_url = source_healine_url.format(source, api_key)
  print('get_sourceHeadlines_url', get_sourceHeadlines_url)

  with urllib.request.urlopen(get_sourceHeadlines_url) as url :
    sourceHeadlines_data = url.read()
    sourceHeadlines_response = json.loads(sourceHeadlines_data)
    print(sourceHeadlines_response)

    sourceHeadlines_results = None

    if sourceHeadlines_response['status'] == 'ok' :
      sourceHeadlines_results_list = sourceHeadlines_response['articles']
      sourceHeadlines_results = process_articles_results(sourceHeadlines_results_list)

  print('topHeadlines_results', sourceHeadlines_results)
  return(sourceHeadlines_results)

def process_topHeadlines_results(topHeadlines_results_list) :
  '''
  process Top headlines results and transform them to a list of objects
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
    '''
    get the json response to  our url request for all the articles
    '''
    get_articles_url = articles_url.format(api_key)

    with urllib.request.urlopen(get_articles_url) as url :
      get_articles_data = url.read()
      get_articles_response = json.loads(get_articles_data)

      articles_results = None

      if get_articles_response['articles']:
        articles_results_list = get_articles_response['articles']
        articles_results = process_articles_results(articles_results_list)
        
    return articles_results

def process_articles_results(articles_results_list):
  '''
  process top articles results and transform them to a list of objects
  '''
  articles_results = []
  for articles_item in articles_results_list :
    author = articles_item.get('author')
    source = articles_item.get('source')
    title = articles_item.get('title')
    description = articles_item.get('description')
    url = articles_item.get('url')
    urlToImage = articles_item.get('urlToImage')
    publishedAt = articles_item.get('publishedAt')
    content = articles_item.get('content')

    articles_object = Articles(source, author, title, description, url, urlToImage, publishedAt, content)
    articles_results.append(articles_object)
     
  return articles_results


def search_article(article):
  search_article_url = 'https://newsapi.org/v2/search/everything?apiKey={}&query={}'.format(api_key,article)
  with urllib.request.urlopen(search_article_url) as url:
      search_article_data = url.read()
      search_article_response = json.loads(search_article_data)

      search_article_results = None

      if search_article_response['results']:
          search_article_list = search_article_response['results']
          search_article_results = process_results(search_article_list)


  return search_article_results