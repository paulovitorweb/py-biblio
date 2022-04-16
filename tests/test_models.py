from src.pybiblio.domain.models import Author, Publication, Bibliography, Book, Article
from tests.utils import lists_are_equal


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
    assert (
        book.reference == 'CAMPAGNI, Roberto. Economia urbana. Barcelona: Ed. Antonio Bosch, 2005.'
    )
    assert str(book) == 'CAMPAGNI, Roberto. Economia urbana. Barcelona: Ed. Antonio Bosch, 2005.'


def test_instance_article(some_authors):
    article = Article(
        4,
        'O transporte urbano de João Pessoa',
        2008,
        [some_authors[3]],
        'Minha Cidade',
        4,
        92,
        8,
        (82, 102),
    )
    assert article.id == 4
    assert article.title == 'O transporte urbano de João Pessoa'
    assert article.year == 2008
    assert article.authors == [Author(4, 'Paulo Freire')]
    assert article.journal == 'Minha Cidade'
    assert article.volume == 4
    assert article.number == 92
    assert article.edition_year == 8
    assert article.citation == '(FREIRE, 2008)'
    assert (
        article.reference
        == 'FREIRE, Paulo. O transporte urbano de João Pessoa. Minha Cidade, Vol. 4, No. 92, Ano 8, 2008. p. 82-102.'
    )
    assert (
        str(article)
        == 'FREIRE, Paulo. O transporte urbano de João Pessoa. Minha Cidade, Vol. 4, No. 92, Ano 8, 2008. p. 82-102.'
    )


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
    assert lists_are_equal(authors, some_authors[0:2])
