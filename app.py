from flask import Flask
from urllib.parse import quote

def create_app():
    app = Flask(_name_)

    @app_route('/')
    def home():
        return quote('Hello, world! This is a simple Flask app 12333.')

    return app

if _name_=='__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
