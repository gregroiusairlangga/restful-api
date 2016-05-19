from flask import Blueprint, request, jsonify, make_response
from app.size.models import Size, SizeSchema, db
from flask_restful import Api, Resource
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

size = Blueprint('size', __name__)
schema = SizeSchema()
api = Api(size)

# Size
class SizeList(Resource):
    def get(self):
        size_query = Size.query.all()
        results = schema.dump(size_query, many=True).data
        return results
    
    def post(self):
        raw_dict = request.get_json(force=True)
        try:
                schema.validate(raw_dict)
                size_dict = raw_dict['data']['attributes']
                size_val = Size(size_dict['size'])
                size_val.add(size_val)            
                query = Size.query.get(size_val.id)
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



class SizeUpdate(Resource):
    def get(self, id):
        size_query = Size.query.get_or_404(id)
        result = schema.dump(size_query).data
        return result
    
    def patch(self, id):
        sizes = Size.query.get_or_404(id)
        raw_dict = request.get_json(force=True)
        
        try:
            schema.validate(raw_dict)
            size_dict = raw_dict['data']['attributes']
            for key, value in size_dict.items():
                
                setattr(sizes, key, value)
          
            sizes.update()            
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
        sizes = Size.query.get_or_404(id)
        db.session.delete(sizes)
        db.session.commit()
        response = make_response()
        response.status_code = 204
        return response
        

api.add_resource(SizeList, '.json')
api.add_resource(SizeUpdate, '/<int:id>.json')