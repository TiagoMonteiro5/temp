import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import pymysql

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

CLOUDSQL_USER='teste_bd'
CLOUDSQL_PASSWORD ="pass_bd"
PUBLIC_IP_ADDRESS ="34.89.60.255"
CLOUDSQL_DATABASE ="bd_reviews"
CLOUDSQL_CONNECTION_NAME ="CN2021-steam-reviews:europe-west2:teste"
INSTANCE_NAME ="teste_bd"
  
# configuration
app.config["SECRET_KEY"] = "yoursecretkey"
app.config["SQLALCHEMY_DATABASE_URI"]=(
    'mysql+pymysql://{nam}:{pas}@34.89.60.255/{dbn}').format (
    nam=CLOUDSQL_USER,
    pas=CLOUDSQL_PASSWORD,
    dbn=CLOUDSQL_DATABASE,
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True
  
db = SQLAlchemy(app)
# Initialize Marshmallow
ma = Marshmallow(app)