import os


class config:
  '''
  General configuration parent class
  '''
  NEWS_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}' 
  SOURCE_HEADLINE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
  NEWS_HIGHLIGHT_API_BASE_URL = 'https://newsapi.org/v2/sources?apikey={}'
  NEWS_EVERYTHING_URL = 'https://newsapi.org/v2/everything?q=trending&language=en&apiKey={}'
  NEWS_HIGHLIGHT_API_KEY=os.environ.get('API_KEY')


class ProdConfig(config):
  '''
  Production configuration child class
  args:
       Config: the parent configuration class with General configuration settings
  '''
  pass

class DevConfig(config):
  '''
  Development configuration child class
  args: 
        config: the parent configuration class with General configuration settings
  '''

  Debug = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}