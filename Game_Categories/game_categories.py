from flask import Flask 
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Game_Categories(Resource):
    def get(self):
        return "This is the game categories"

api.add_resource(Game_Categories, '/')

if __name__ == '__main__':     
	app.run(debug=True, host='0.0.0.0')