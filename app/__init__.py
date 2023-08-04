from flask import Flask
from app.api.routes import api
from config import Config
from app.site.routes import site

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db as root_db, Migrate
from flask_cors import CORS
from .helpers import JSONEncoder

app = Flask(__name__)
app.register_blueprint( api )
app.register_blueprint(site)
app.config.from_object(Config)

app.config.from_object( Config )

root_db.init_app( app )
migrate=Migrate( app, root_db )

app.json_encoder=JSONEncoder
CORS( app )