import pytest
from src.pybiblio.models import Author, Publication, Bibliography, Book


@pytest.fixture
def some_authors():
    return [
        Author(1, 'Paulo de Freitas'), 
        Author(2, 'Alexandre de Castro'),
        Author(3, 'Roberto Campagni')
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


def test_instance_author():
    author = Author(1, 'Paulo de Freitas')
    assert author.id == 1
    assert author.name == 'Paulo de Freitas'
    assert author.citation == 'FREITAS'
    assert author.reference == 'FREITAS, Paulo de'
    assert str(author) == 'FREITAS, Paulo de'


def test_instance_publication(some_authors):
    publication = Publication(1, 'A Rede Urbana', 2016, some_authors[0:2])
    assert publication.id == 1
    assert publication.title == 'A Rede Urbana'
    assert publication.year == 2016
    assert publication.authors == [Author(1, 'Paulo de Freitas'), Author(2, 'Alexandre de Castro')]
    assert publication.citation == '(FREITAS; CASTRO, 2016)'
    assert publication.reference == 'FREITAS, Paulo de; CASTRO, Alexandre de. A Rede Urbana, 2016.'
    assert str(publication) == 'FREITAS, Paulo de; CASTRO, Alexandre de. A Rede Urbana, 2016.'

def test_instance_book(some_authors):
    book = Book(3, 'Economia urbana', 2005, some_authors[2:3], 'Barcelona', 'Ed. Antonio Bosch')
    assert book.id == 3
    assert book.title == 'Economia urbana'
    assert book.year == 2005
    assert book.authors == [Author(3, 'Roberto Campagni')]
    assert book.location == 'Barcelona'
    assert book.publishing_company == 'Ed. Antonio Bosch'
    assert book.citation == '(CAMPAGNI, 2005)'
    assert book.reference == 'CAMPAGNI, Roberto. Economia urbana. Barcelona: Ed. Antonio Bosch, 2005.'
    assert str(book) == 'CAMPAGNI, Roberto. Economia urbana. Barcelona: Ed. Antonio Bosch, 2005.'
    

def test_instance_bibliography(some_publications, some_authors):
    biblio = Bibliography(some_publications)
    expected_text = (
        '<ul>'
            '<li>FREITAS, Paulo de; CASTRO, Alexandre de. A Rede Urbana, 2016.</li>'
            '<li>FREITAS, Paulo de. Ecossistema GIS, 2020.</li>'
        '</ul>'
    )
    assert biblio.as_html() == expected_text
    authors = biblio.get_authors()
    assert len(authors) == 2 and all(author in authors for author in some_authors[0:2])