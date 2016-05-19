from flask import Blueprint, request, jsonify, make_response
from app.category.models import Category,CategorySchema, db
from flask_restful import Api, Resource
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

category = Blueprint('category', __name__)
schema = CategorySchema()
api = Api(category)

# Category
class CategoryList(Resource):
    def get(self):
        category_query = Category.query.all()
        results = schema.dump(category_query, many=True).data
        return results
    
    def post(self):
        raw_dict = request.get_json(force=True)
        try:
                schema.validate(raw_dict)
                category_dict = raw_dict['data']['attributes']
                category_val = Category(category_dict['category'])
                category_val.add(category_val)    
                #category_val.add(category_val)            
                query = Category.query.get(category_val.id)
                results = schema.dump(query).data                
                return results, 201
                #db.session.add(category_val)
                #db.session.commit()      
                #resp = jsonify({"sukses": "Success Insert Data"})              
                #return resp, 201
            
        except ValidationError as err:
                resp = jsonify({"error": err.messages})
                resp.status_code = 404
                return resp               
                
        except SQLAlchemyError as e:
                db.session.rollback()
                resp = jsonify({"error": str(e)})
                resp.status_code = 403
                return resp
        

class CategoryUpdate(Resource):
    
    def get(self, id):
        category_query = Category.query.get_or_404(id)
        result = schema.dump(category_query).data
        return result
    
    def patch(self, id):
        categorys = Category.query.get_or_404(id)
        raw_dict = request.get_json(force=True)
        
        try:
            schema.validate(raw_dict)
            category_dict = raw_dict['data']['attributes']
            for key, value in category_dict.items():
                
                setattr(categorys, key, value)
          
            categorys.update()            
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
        categorys = Category.query.get_or_404(id)
        db.session.delete(categorys)
        db.session.commit()
        response = make_response()
        response.status_code = 204
        return response
            
api.add_resource(CategoryList, '.json')
api.add_resource(CategoryUpdate, '/<int:id>.json')