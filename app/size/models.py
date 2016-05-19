from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from app.crud import CRUD

db = SQLAlchemy()


class Size(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(250), unique=True, nullable=False)   

    def __init__(self,  size):
        self.size = size
      
           
class SizeSchema(Schema):
    id = fields.Integer(dump_only=True)
    size = fields.String()    
 
    
     #self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/size/"
        else:
            self_link = "/size/{}".format(data['id'])
        return {'self': self_link}
   
    
    class Meta:
        type_ = 'size'
        