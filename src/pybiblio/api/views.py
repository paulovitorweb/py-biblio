from fastapi import HTTPException
from src.pybiblio.infrastructure import repository
from src.pybiblio.infrastructure.orm import Session
from src.pybiblio.domain.models import Author, Book
from . import schemas


def get_author(db: Session, author_id: int):
    author = repository.AuthorRepository(session=db).get(author_id)
    if author is None:
        raise HTTPException(404, f'Author with id {author_id} not found')
    return author


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = Author(name=author.name)
    repository.AuthorRepository(session=db).add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_authors(db: Session):
    return repository.AuthorRepository(session=db).list()


def get_book(db: Session, book_id: int):
    book = repository.BookRepository(session=db).get(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail='Book not found')
    return book
