from typing import List
from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int
    citation: str
    reference: str

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    year: int
    publishing_company: str
    location: str


class BookCreate(BookBase):
    authors: List[int]


class Book(BookBase):
    id: int
    authors: List[Author]
    citation: str
    reference: str

    class Config:
        orm_mode = True
