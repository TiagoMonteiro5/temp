from flask import make_response, abort,json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from config import db
from models import (Game)

def read_all():
    """[Function to retrieve all values from the table game of the db_reviews]

    Returns:
        [json]: [All values from the table games]
    """
    g = Game.query.all()
    return json.jsonify(g.serialize())

def read_one(game_id):
    """Search game by game_id

    Args:
        game_id (inte): [game_id to search the game]

    Returns:
        [json]: [return json with the game_id and game_name]
    """
    #Verifica se userID existe
    g = Review_Category.query.filter(Review_Category.review_id == reviewID)

    if g is not None:
        return json.datetime(g.serialize())
    else:
        abort(404, 'Theres no review with that id')   

# Criar nova review 
def create(game_name):
    pass

def delete(reviewID):
    review = REVIEWS[reviewID]
    if review in REVIEWS:
        del REVIEWS[reviewID]
    else:
        abort(404, "This UserID does not exists")