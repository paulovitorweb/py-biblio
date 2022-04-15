from typing import List

from fastapi import Depends, FastAPI
from fastapi.openapi.utils import get_openapi
from sqlalchemy.orm import Session

from src.pybiblio.infrastructure.orm import DbSession, init_db
from . import schemas, views


init_db()


app = FastAPI()


def get_db():
    db = DbSession()
    try:
        yield db
    finally:
        db.close()


@app.post('/authors/', response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return views.create_author(db, author=author)


@app.get('/authors/', response_model=List[schemas.Author])
def read_authors(db: Session = Depends(get_db)):
    return views.get_authors(db)


@app.get('/authors/{author_id}', response_model=schemas.Author)
def read_author(author_id: int, db: Session = Depends(get_db)):
    return views.get_author(db, author_id=author_id)


@app.get('/books/', response_model=List[schemas.Book])
def read_books(db: Session = Depends(get_db)):
    return views.get_books(db)


@app.get('/books/{book_id}', response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    return views.get_book(db, book_id=book_id)


@app.post('/books/', response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return views.create_book(db, book=book)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title='PyBiblio',
        version='0.1.0',
        description='Uma aplicação escrita em Python para gerenciar referências bibliográficas.',
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
