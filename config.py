from os import environ, path


class Config:
  '''
  General configuration parent class
  '''
  NEWS_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
  SOURCE_HEADLINE_URL = 'https://newsapi.org/v2/top-headlines/sources={}apiKey={}'
  NEWS_HIGHLIGHT_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
  NEWS_EVERYTHING_URL = 'https://newsapi.org/v2/everything?q=trending&language=en&api={}'
  NEWS_HIGHLIGHT_API_KEY= environ.get('NEWS_API_KEY')

class ProdConfig(Config):
  '''
   Production  configuration child class
   Args:
       Config:The parent configuration class with General configuration settings
  '''
  pass

class DevConfig(Config):
  '''
  Development configuration child class
  Args:
      Config: The parent configuration class with General configuration settigs
  '''
  DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
