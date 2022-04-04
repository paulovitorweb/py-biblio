import abc
from typing import List
from sqlalchemy.orm import Session
from src.pybiblio.models import Author, Book


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


class BookRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, book: Book):
        """Add a book to the database"""
        self.session.add(book)

    def get(self, id) -> Book:
        """Retrieve a book from the database by id"""
        return self.session.query(Book).filter_by(id=id).one()

    def list(self) -> List[Book]:
        """Retrieve all books from the database"""
        return self.session.query(Book).all()
