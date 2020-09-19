import json

from flask import make_response, jsonify
from flask_restful import Resource, reqparse

from web_scraping.models import ScrapingData


class Scraping(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()

    def get(self):
        scrapings_data = ScrapingData.query.filter()
        return make_response(jsonify(data=json.loads(scrapings_data)), 200)

    def post(self):
        self.parser.add_argument('name', type=str, location='parm')
        self.parser.add_argument('data', type=str)
        args = self.parser.parse_args()
        scraping = ScrapingData(name=args.name, data=args.data)
        scraping.save()
        return make_response(jsonify(status=200), 201)