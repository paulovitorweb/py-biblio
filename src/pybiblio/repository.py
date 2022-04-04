import abc
from src.pybiblio.models import Author


class AuthorAbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, author: Author):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, id) -> Author:
        raise NotImplementedError


class AuthorRepository(AuthorAbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, author: Author):
        self.session.add(author)

    def get(self, id) -> Author:
        return self.session.query(Author).filter_by(id=id).one()
