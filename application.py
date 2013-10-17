import flask
from models import db
from data import test
from api import api

def create_app():
    app = flask.Flask("app")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    app.register_blueprint(api)
    db.app=app
    db.init_app(app)
    db.create_all()
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
