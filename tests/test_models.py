import pytest
from src.pybiblio.models import Author, Publication, Bibliography


@pytest.fixture
def some_authors():
    return [Author('Paulo de Freitas'), Author('Alexandre de Castro')]


@pytest.fixture
def some_publications(some_authors):
    return [Publication('A Rede Urbana', 2016, some_authors)]


def test_instance_author(some_authors):
    author = some_authors[0]
    assert author.name == 'Paulo de Freitas'
    assert author.citation == 'FREITAS'
    assert author.reference == 'FREITAS, Paulo de'
    assert str(author) == 'FREITAS, Paulo de'


def test_instance_publication(some_publications):
    publication = some_publications[0]
    assert publication.title == 'A Rede Urbana'
    assert publication.year == 2016
    assert publication.authors == [Author('Paulo de Freitas'), Author('Alexandre de Castro')]
    assert publication.citation == '(FREITAS; CASTRO, 2016)'
    assert publication.reference == 'FREITAS, Paulo de; CASTRO, Alexandre de. A Rede Urbana, 2016.'
    assert str(publication) == 'FREITAS, Paulo de; CASTRO, Alexandre de. A Rede Urbana, 2016.'

def test_instance_bibliography(some_publications):
    biblio = Bibliography(some_publications)
    expected_text = (
        '<ul>'
            '<li>FREITAS, Paulo de; CASTRO, Alexandre de. A Rede Urbana, 2016.</li>'
        '</ul>'
    )
    assert biblio.as_html() == expected_text