from flask import Flask
from flask_restful import Api, Resource
from sqlalchemy import create_engine

app = Flask(__name__)
engine = create_engine('sqlite:///sales.db', echo = True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

api = Api(app)

@app.route('/') 
def home():
	return "Hello, world!"

users = []
id = 0

class UserAPI(Resource):
    def get(self, name):
        for user in users:
            if user['name'] == name:
                return user
    def post(self, name):
        global id
        user = {'name' : name, 'id' : id}
        id += 1
        users.append(user)
        return user

api.add_resource(UserAPI, '/users/<string:name>', endpoint = 'user')

app.run(port=5000)