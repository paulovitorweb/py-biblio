import abc
from typing import List
from sqlalchemy.orm import Session
from src.pybiblio.models import Author


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, obj):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, id):
        raise NotImplementedError


class AuthorRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, author: Author):
        """Add an author to the database"""
        self.session.add(author)

    def get(self, id) -> Author:
        """Retrieve an author from the database by id"""
        return self.session.query(Author).filter_by(id=id).one()

    def list(self) -> List[Author]:
        """Retrieve all authors from the database"""
        return self.session.query(Author).all()
