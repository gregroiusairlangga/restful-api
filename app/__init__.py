from flask import Flask, Response

class MyResponse(Response):
     default_mimetype = 'application/xml'
     
    
def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.response_class = MyResponse

    from app.users.models import db
    from app.color.models import db
    from app.size.models import db
    from app.product.models import db
    from app.category.models import db

    db.init_app(app)

    # Blueprints   
    from app.users.views import users
    from app.color.views import color
    from app.size.views import size
    from app.product.views import product
    from app.category.views import category

    app.register_blueprint(users, url_prefix='/api/v1/users')
    app.register_blueprint(color, url_prefix='/api/v1/color')
    app.register_blueprint(size, url_prefix='/api/v1/size')
    app.register_blueprint(product, url_prefix='/api/v1/product')
    app.register_blueprint(category, url_prefix='/api/v1/category')
    

    return app
    