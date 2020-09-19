import json
import os
import pathlib

from flask import make_response
from flask_restful import Resource, reqparse


class Rest(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()

    def get(self):
        with open(os.path.join(pathlib.Path(__file__).parent.absolute(), 'data.txt'), 'r') as o:
            data = o.read()
        return make_response(json.loads(data))



