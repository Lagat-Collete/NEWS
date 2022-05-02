from app import app
import urllib.request,json
from .models import news


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