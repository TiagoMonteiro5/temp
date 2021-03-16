# Returns highly-rated games with low amount of reviews

from flask import Flask 
from flask_restful import Resource, Api 

app = Flask(__name__) 
api = Api(app) 

class HiddenGems(Resource): 
	def get(self): 
		return "Discover these hidden gems!"
		
# lista com jogos com poucas reviews mas score muito positivo ou muitas horas jogadas
		
api.add_resource(HiddenGems, '/') 
if __name__ == '__main__':     
	app.run(debug=True, host='0.0.0.0')
	




