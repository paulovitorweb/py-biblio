from fastapi import HTTPException
from src.pybiblio.infrastructure import repository
from src.pybiblio.infrastructure.orm import Session


def get_author(db: Session, author_id: int):
    author = repository.AuthorRepository(session=db).get(author_id)
    if author is None:
        raise HTTPException(404, f'Author with id {author_id} not found')
    return author
