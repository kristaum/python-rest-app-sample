from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Requests(Resource):
    def get(self):
        return {'Resp': 'App is up and working'}, 200  # return data and 200 OK

    def post(self):
        return request.json, 200  # return data with 200 OK
                    

api.add_resource(Requests, '/requests')  # add endpoints

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)  # run our Flask app