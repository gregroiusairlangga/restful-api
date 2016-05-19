from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from app.crud import CRUD

db = SQLAlchemy()

class Category(db.Model,CRUD):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.Text)

    def __init__(self,category):
        self.category = category

    def __repr__(self):
        return self.category
           
class CategorySchema(Schema):
    id = fields.Integer(dump_only=True)
    category=fields.String()
 
     #self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/category/"
        else:
            self_link = "/category/{}".format(data['id'])
        return {'self': self_link}
   
    
    class Meta:
        type_ = 'category'
        