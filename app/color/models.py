from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from app.crud import CRUD

db = SQLAlchemy()

class Color(db.Model,CRUD):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.Text)

    def __init__(self,color):
        self.color = color

    def __repr__(self):
        return self.color
           
class ColorSchema(Schema):
    id = fields.Integer(dump_only=True)
    color=fields.String()
 
     #self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/color/"
        else:
            self_link = "/color/{}".format(data['id'])
        return {'self': self_link}
   
    
    class Meta:
        type_ = 'color'
        