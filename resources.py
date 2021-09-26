from flask import jsonify
from flask_restful import Resource
from models import Author, Reference
from db import db_session as session


class AuthorResource(Resource):
    def get(self, id: int):
      author = session.query(Author).filter_by(id=id).first()
      return jsonify(author)


class AuthorListResource(Resource):
    def get(self):
        authors = session.query(Author).all()
        return jsonify(authors=authors)


class ReferenceResource(Resource):
    def get(self, id: int):
      reference = session.query(Reference).filter_by(id=id).first()
      return jsonify(reference)


class ReferenceListResource(Resource):
    def get(self):
        references = session.query(Reference).all()
        return jsonify(references=references)