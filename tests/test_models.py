import pytest
from src.pybiblio.models import Author, Publication, Bibliography


@pytest.fixture
def some_authors():
    return [Author(1, 'Paulo de Freitas'), Author(2, 'Alexandre de Castro')]


@pytest.fixture
def some_publications(some_authors):
    return [
        Publication(1, 'A Rede Urbana', 2016, some_authors),
        Publication(2, 'Ecossistema GIS', 2020, some_authors[0:1])
    ]


def test_instance_author(some_authors):
    author = some_authors[0]
    assert author.id == 1
    assert author.name == 'Paulo de Freitas'
    assert author.citation == 'FREITAS'
    assert author.reference == 'FREITAS, Paulo de'
    assert str(author) == 'FREITAS, Paulo de'


def test_instance_publication(some_publications):
    publication = some_publications[0]
    assert publication.id == 1
    assert publication.title == 'A Rede Urbana'
    assert publication.year == 2016
    assert publication.authors == [Author(1, 'Paulo de Freitas'), Author(2, 'Alexandre de Castro')]
    assert publication.citation == '(FREITAS; CASTRO, 2016)'
    assert publication.reference == 'FREITAS, Paulo de; CASTRO, Alexandre de. A Rede Urbana, 2016.'
    assert str(publication) == 'FREITAS, Paulo de; CASTRO, Alexandre de. A Rede Urbana, 2016.'

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
    assert len(authors) == 2 and all(author in authors for author in some_authors)