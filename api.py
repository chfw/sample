import flask
from data import test
from models import db

api = flask.Blueprint("api",__name__,template_folder="templates")

@api.route("/")
def helloworld():
    t = test(ab="aa")
    db.session.add(t)
    db.session.commit()
    return t.ab+str(t.id)
