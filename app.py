from flask import Flask
from flask_restful import Api
from db import db_session, init_db
from resources import AuthorListResource, AuthorResource, ReferenceResource, \
    ReferenceListResource

app = Flask(__name__)
api = Api(app)

init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

api.add_resource(AuthorListResource, '/authors')
api.add_resource(AuthorResource, '/author/<int:id>')
api.add_resource(ReferenceListResource, '/references')
api.add_resource(ReferenceResource, '/reference/<int:id>')