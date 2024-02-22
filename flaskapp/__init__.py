from flask import Flask
from flaskapp.routes import changelog, service, changeset

projects = {}

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(changelog)
    app.register_blueprint(service)
    app.register_blueprint(changeset)
    return app