from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
@app.route("/")
@app.route("/reviews")

class reviews(Resource):
    def get(self):
        return "All Reviews"
    def game(id):
        return "Reviews from game "+id

api.add_resource(reviews, '/')

if __name__ == '__main__':     
	app.run(debug=True, host='0.0.0.0')