import flask

api = flask.Blueprint("api",__name__,template_folder="templates")

@api.route("/")
def helloworld():
    return "hello world"
