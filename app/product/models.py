from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from app.crud import CRUD

db = SQLAlchemy()

class Product(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(250))
    id_size = db.Column(db.Integer)
    id_color = db.Column(db.Integer)
    price = db.Column(db.Float)
    id_category = db.Column(db.Integer)
    gambar = db.Column(db.String(250))

    def __init__(self, name,id_size,id_color,price,id_category,gambar):
        self.name=name
        self.id_size=id_size
        self.id_color=id_color
        self.price=price
        self.id_category=id_category
        self.gambar=gambar
      
           
class ProductSchema(Schema):
    id = fields.Integer(dump_only=True)
    name=fields.String()
    id_size=fields.Integer()
    id_color=fields.Integer()
    price=fields.Float()
    id_category=fields.Integer()
    gambar=fields.String()
 
    
     #self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/product/"
        else:
            self_link = "/product/{}".format(data['id'])
        return {'self': self_link}
   
    
    class Meta:
        type_ = 'product'
        