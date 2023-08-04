from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow 
import secrets

db =SQLAlchemy()
ma=Marshmallow()


class UserImages(db.Model):
    entry_id = db.Column(db.String, primary_key = True)
    url = db.Column(db.String(200))
    user_id = db.Column(db.String(200))
    prio = db.Column(db.Numeric(precision=10,scale=0))

    def __init__(self, url,user_id,prio ,entry_id = ''):
        self.entry_id = self.set_id()
        self.url = url
        self.user_id = user_id
        self.prio = prio


    def __repr__(self):
        return f"The following url has been added to {self.user_id}'s collection: {self.url}"

    def set_id(self):
        return (secrets.token_urlsafe())

class UserImagesSchema(ma.Schema):
    class Meta:
        fields = ['entry_id','url', 'user_id','prio']

uIm_schema = UserImagesSchema()
uIm_schemas = UserImagesSchema(many=True)