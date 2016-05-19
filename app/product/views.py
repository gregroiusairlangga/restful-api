from flask import Blueprint, request, jsonify, make_response
from app.product.models import Product, ProductSchema, db
from flask_restful import Api, Resource
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

product = Blueprint('product', __name__)
schema = ProductSchema()
api = Api(product)

# Product
class ProductList(Resource):
    def get(self):
        product_query = Product.query.all()
        results = schema.dump(product_query, many=True).data
        return results
    
    def post(self):
        raw_dict = request.get_json(force=True)
        try:
                schema.validate(raw_dict)
                product_dict = raw_dict['data']['attributes']
                product_val = Product(product_dict['name'],product_dict['id_size'],product_dict['id_color'],product_dict['price'],product_dict['id_category'],product_dict['gambar'])
                product_val.add(product_val)            
                query = Product.query.get(product_val.id)
                results = schema.dump(query).data                
                return results, 201
            
        except ValidationError as err:
                resp = jsonify({"error": err.messages})
                resp.status_code = 403
                return resp               
                
        except SQLAlchemyError as e:
                db.session.rollback()
                resp = jsonify({"error": str(e)})
                resp.status_code = 403
                return resp


class ProductFilterSize(Resource):
    def get(self,id_size):
        product_query = Product.query.filter_by(id_size=id_size).first() 
        #product_query = Product.query.filter_by(id_size=id).all() #jalankan kode berikut untuk menampilkan banyak item
        result = schema.dump(product_query).data
        return result  

class ProductFilterColor(Resource):
    def get(self,id_color):
        product_query = Product.query.filter_by(id_color=id_color).first() 
        #product_query = Product.query.filter_by(id_color==id).all() #jalankan kode berikut untuk menampilkan banyak item
        result = schema.dump(product_query).data
        return result  

class ProductFilterPrice(Resource):
    def get(self,pricemin,pricemax):
        product_query = Product.query.filter(price>=pricemin,price<=pricemax).all()
        #product_query = Product.query.filter(price>=pricemin,price<=pricemax).all() #jalankan kode berikut untuk menampilkan banyak item
        result = schema.dump(product_query).data
        return result  

class ProductUpdate(Resource):
    
    def get(self, id):
        product_query = Product.query.get_or_404(id)
        result = schema.dump(product_query).data
        return result    

    #def getByIdSize():

    #def getByIdColor():

    #def getByPrice(self,pricemin):

    #def getFilterPrice():


    def patch(self, id):
        product = Product.query.get_or_404(id)
        raw_dict = request.get_json(force=True)
        
        try:
            schema.validate(raw_dict)
            product_dict = raw_dict['data']['attributes']
            for key, value in product_dict.items():
                
                setattr(product, key, value)
          
            product.update()            
            return self.get(id)
            
        except ValidationError as err:
                resp = jsonify({"error": err.messages})
                resp.status_code = 401
                return resp               
                
        except SQLAlchemyError as e:
                db.session.rollback()
                resp = jsonify({"error": str(e)})
                resp.status_code = 401
                return resp
         
    def delete(self, id):
        products = Product.query.get_or_404(id)
        db.session.delete(products)
        db.session.commit()
        response = make_response()
        response.status_code = 204
        return response
        

api.add_resource(ProductList, '.json')
api.add_resource(ProductUpdate, '/<int:id>.json')
api.add_resource(ProductFilterSize, '/getbysize/<int:id_size>.json')
api.add_resource(ProductFilterColor, '/getbycolor/<int:id_color>.json')
api.add_resource(ProductFilterPrice, '/filterprice/<int:pricemin>-<int:pricemax>.json')