import pytest
from src.pybiblio.orm import InMemorySession, in_memory_engine, metadata
from src.pybiblio.models import Author, Publication, Book, Article


@pytest.fixture
def session():
    metadata.create_all(in_memory_engine)
    yield InMemorySession()
    metadata.drop_all(in_memory_engine)


@pytest.fixture
def some_authors():
    return [
        Author(1, 'Paulo de Freitas'), 
        Author(2, 'Alexandre de Castro'),
        Author(3, 'Roberto Campagni'),
        Author(4, 'Paulo Freire')
    ]


@pytest.fixture
def some_publications(some_authors):
    return [
        Publication(1, 'A Rede Urbana', 2016, some_authors[0:2]),
        Publication(2, 'Ecossistema GIS', 2020, some_authors[0:1])
    ]


@pytest.fixture
def some_books(some_authors):
    return [
        Book(3, 'Economia urbana', 2005, some_authors[2:3], 'Barcelona', 'Ed. Antonio Bosch')
    ]


@pytest.fixture
def some_articles(some_authors):
    return [
        Article(4, 'O transporte urbano de João Pessoa', 2008, [some_authors[3]], 4, 92, 8)
    ]
