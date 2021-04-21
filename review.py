from flask import Flask, jsonify, request
from db_connector import get_reviews
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "entrada"


@app.route('/reviews/<int:reviews_id>', methods=['GET'])
def get_review(reviews_id):
    if request.method == 'GET':
        get_reviews(reviews_id)
    else:
        return 'Só funciona com metodo GET'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=int(os.environ.get('PORT', 8080)), debug=True)
