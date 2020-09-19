from flask import Blueprint
from flask_restful import Api

web_scraping = Blueprint('web_scraping', __name__, url_prefix='/scraping')
api_scraping = Api(web_scraping)
from .routers import *