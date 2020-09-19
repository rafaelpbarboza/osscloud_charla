from flask import Blueprint
from flask_restful import Api

json_bp = Blueprint('json_bp', __name__, url_prefix='/json')
api_json = Api(json_bp)

from .routers import *
