# Returns games that are similar to the one chosen by the user

from flask import Flask 
from flask_restful import Resource, Api 

app = Flask(__name__) 
api = Api(app) 

class Recommend(Resource): 
	def get(self): 
		return "Some games you might enjoy:"
		
# lista dos melhores jogos semelhantes em género ou categoria a um jogo indicado pelo utilizador
		
api.add_resource(Recommend, '/') 
if __name__ == '__main__':     
	app.run(debug=True, host='0.0.0.0')
	




