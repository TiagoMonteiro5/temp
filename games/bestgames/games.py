# Returns the top 100 games on Steam, ordered by Rating

from flask import Flask 
from flask_restful import Resource, Api 

app = Flask(__name__) 
api = Api(app) 

class BestGames(Resource): 
	def get(self): 
		return "These are the best games on Steam!"
		
api.add_resource(BestGames, '/') 
if __name__ == '__main__':     
	app.run(debug=True, host='0.0.0.0')
	




