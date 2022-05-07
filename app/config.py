from instance.config import NEWS_API_KEY


class Config:
  '''
  General configuration parent class
  '''
  NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?apikey={}'

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
