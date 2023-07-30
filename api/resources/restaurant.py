import logging
from flask import request
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound
from api.database import db
from api.models.models import Restaurant
from api.schemas.schema import RestaurantSchema

logger = logging.getLogger(__name__)

RESTAURANT_ENDPOINT = "/restaurants/<int:id>"


class RestaurantResource(Resource):
    """
    Restaurant route methods
    """
    def get(self):
        """
        RestaurantResource GET method.
        """
        id = request.view_args.get('id')

        if not id:
            return "please provide an id", 400

        try:
            return self._get_restaurant_by_id(id), 200
        except NoResultFound:
            abort(404, message="Restaurant not found.")

    def post(self):
        """
        RestaurantResource POST method.
        """
        data = request.get_json()

        if not data:
            return "No data to post", 400

        try:
            restaurant = self._create_restaurant(data)
            return restaurant, 201
        except Exception as e:
            return str(e), 500

    def put(self):
        """
        RestaurantResource PUT method.
        """
        id = request.view_args.get('id')
        data = request.get_json()

        if not id or not data:
            return "No id given", 400

        try:
            restaurant = self._update_restaurant(id, data)
            return restaurant, 200
        except NoResultFound:
            abort(404, message="Restaurant not found.")
        except Exception as e:
            return str(e), 500

    def delete(self):
        """
        RestaurantResource DELETE method.
        """
        id = request.view_args.get('id')

        if not id:
            return "No id given", 400

        try:
            self._delete_restaurant(id)
            return "", 204
        except NoResultFound:
            abort(404, message="Restaurant not found.")
        except Exception as e:
            return str(e), 500

    def _get_restaurant_by_id(self, id):
        restaurants = Restaurant.query.filter_by(id=id).first()

        if restaurants is None:
            raise NoResultFound

        restaurant_json = RestaurantSchema().dump(restaurants)
        return restaurant_json

    def _create_restaurant(self, data):
        # Create a new restaurant instance from the data and save it to the database
        restaurant = Restaurant(**data)
        db.session.add(restaurant)
        db.session.commit()
        return RestaurantSchema().dump(restaurant)

    def _update_restaurant(self, id, data):
        restaurant = Restaurant.query.filter_by(id=id).first()

        if restaurant is None:
            raise NoResultFound

        # Update the restaurant attributes with the new data
        for key, value in data.items():
            setattr(restaurant, key, value)

        db.session.commit()
        return RestaurantSchema().dump(restaurant)

    def _delete_restaurant(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()

        if restaurant is None:
            raise NoResultFound

        db.session.delete(restaurant)
        db.session.commit()
