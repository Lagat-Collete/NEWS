from flask import Flask
from  config import config_options

def create_app(config_name):
  app = Flask(__name__)
  #newsapi = NewsApiClient
  #creating app configurations
  app.config.from_object(config_options[config_name])
  app.config.from_pyfile('config.py')
  #Initializing flask extensions


  #Registering blueprint
  from .main import main as main_blueprint

  app.register_blueprint(main_blueprint)

  #setting config
  from.request import configure_request
  configure_request(app)

  return app
