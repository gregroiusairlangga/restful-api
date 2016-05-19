from flask import Blueprint, request, jsonify, make_response
from app.color.models import Color, ColorSchema, db
from flask_restful import Api, Resource
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

color = Blueprint('color', __name__)
schema = ColorSchema()
api = Api(color)

# Color
class ColorList(Resource):
    def get(self):
        color_query = Color.query.all()
        results = schema.dump(color_query, many=True).data
        return results
    
    def post(self):
        raw_dict = request.get_json(force=True)
        try:
                schema.validate(raw_dict)
                color_dict = raw_dict['data']['attributes']
                color_val = Color(color_dict['color'])
                color_val.add(color_val)    
                #category_val.add(category_val)            
                query = Color.query.get(color_val.id)
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


class ColorUpdate(Resource):
    
    
    def get(self, id):
        color_query = Color.query.get_or_404(id)
        result = schema.dump(color_query).data
        return result
    
    def patch(self, id):
        color = Color.query.get_or_404(id)
        raw_dict = request.get_json(force=True)
        
        try:
            schema.validate(raw_dict)
            color_dict = raw_dict['data']['attributes']
            for key, value in color_dict.items():
                
                setattr(color, key, value)
          
            color.update()            
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
        colors = Color.query.get_or_404(id)
        db.session.delete(colors)
        db.session.commit()
        response = make_response()
        response.status_code = 204
        return response
        

api.add_resource(ColorList, '.json')
api.add_resource(ColorUpdate, '/<int:id>.json')