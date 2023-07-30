import logging

from flask_restful import Resource


TEST_ENDPOINT = "/"
logger = logging.getLogger(__name__)


class TestResource(Resource):
    def get(self):
        return "Hello, looks like everything's cool"
        