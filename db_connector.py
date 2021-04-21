#db.py
import os
import pymysql
import mysql.connector
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    connection = pymysql.connect(
        unix_socket='/cloudsql/CN2021-steam-reviews:europe-west2:teste',
        user=db_user,
        password=db_password,
        db=db_name,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    return connection


def get_reviews(id):
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM review WHERE id=(%s);', (id))
        reviews = cursor.fetchall()
        if result > 0:
            got_reviews = jsonify(reviews)
        else:
            got_reviews = 'No reviews in DB'
    conn.close()
    return got_reviews