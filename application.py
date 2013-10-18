import flask
from models import db
from data import test
from api import api

def create_app():
    app = flask.Flask("app")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    app.register_blueprint(api)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
