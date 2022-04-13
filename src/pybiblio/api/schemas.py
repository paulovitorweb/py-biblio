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
