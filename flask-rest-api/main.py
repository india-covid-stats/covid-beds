from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class StateOnly(Resource):
    def get(self, state):               #This is for state-wide data retrieval
        return {state: 'state'}          #Will add code once we finalise

class StateCity(Resource):
    def get(self, state, city):               #This is for city specific data retrieval
        return {state: 'city'}          #Will add code once we finalise


api.add_resource(StateOnly, '/<string:state>')
api.add_resource(StateCity, '/<string:state>/<string:city>')

if __name__ == '__main__':
    app.run(debug=True)
