#!/usr/bin/env python
from app import create_app

app = create_app('config')

@app.route('/')
def index():
    return Flask.jsonify({'Message':'hai, welcome in distro app restful api'})

if __name__ == '__main__':
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])
