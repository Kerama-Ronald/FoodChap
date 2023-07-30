
import logging

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from api.database import db
from api.models.models import Restaurant
from api.schemas.schema import RestaurantSchema

logger = logging.getLogger(__name__)

RESTAURANTS_ENDPOINT = "/restaurants"


class RestaurantsResource(Resource):
    def get(self):
        """
        RestaurantsResource GET method.
        """
        try:
            return self._get_all_restaurants(id), 200
        except NoResultFound:
            abort(404, message="Restaurants not found.")

    def _get_all_restaurants(self):
        restaurants = Restaurant.query.all()
        restaurants_json = [RestaurantSchema().dump(restaurant)
                            for restaurant in restaurants]

        return restaurants_json
