from flask import request
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound

from api.database import db

class CustomerResource(Resource):
    """
    Customer route methods
    """
    def get(self, customer_id=None):
        """
        CustomerResource GET method.
        """
        if customer_id:
            # If customer_id is provided, fetch a specific customer by ID
            try:
                return self._get_customer_by_id(customer_id), 200
            except NoResultFound:
                abort(404, message="Customer not found.")
        else:
            # If no customer_id is provided, handle searching for customers based on email
            email = request.args.get("email")

            if email:
                try:
                    return self._get_customer_by_email(email), 200
                except NoResultFound:
                    abort(404, message="Customer not found.")

            return "No search criteria provided", 400

    def post(self):
        """
        CustomerResource POST method.
        """
        data = request.get_json()

        if not data:
            return "No data to post", 400

        try:
            customer = self._create_customer(data)
            return customer, 201
        except Exception as e:
            return str(e), 500

    def put(self, customer_id):
        """
        CustomerResource PUT method.
        """
        data = request.get_json()

        if not data:
            return "No data to update", 400

        try:
            customer = self._update_customer(customer_id, data)
            return customer, 200
        except NoResultFound:
            abort(404, message="Customer not found.")
        except Exception as e:
            return str(e), 500

    def delete(self, customer_id):
        """
        CustomerResource DELETE method.
        """
        try:
            self._delete_customer(customer_id)
            return "", 204
        except NoResultFound:
            abort(404, message="Customer not found.")
        except Exception as e:
            return str(e), 500