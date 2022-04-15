import pytest
from fastapi import HTTPException
from src.pybiblio.infrastructure import repository
from src.pybiblio.domain.models import Author, Book
from src.pybiblio.api import views
from src.pybiblio.api import schemas


def test_get_author_should_succeed(mocker):
    db = mocker.MagicMock()
    mocker.patch.object(repository.AuthorRepository, 'get', return_value=Author(1, 'Paulo Freitas'))
    assert views.get_author(db, 1) == Author(1, 'Paulo Freitas')


def test_get_author_should_raise_error(mocker):
    db = mocker.MagicMock()
    mocker.patch.object(repository.AuthorRepository, 'get', return_value=None)
    with pytest.raises(HTTPException):
        views.get_author(db, 1)


def test_create_author_should_succeed(mocker):
    db = mocker.MagicMock()
    author_create = schemas.AuthorCreate(name='Son Goku')

    def refresh_author(author):
        author.id = 2

    db.refresh.side_effect = refresh_author
    add_method = mocker.patch.object(repository.AuthorRepository, 'add')

    author = views.create_author(db, author_create)
    add_method.assert_called_once()
    db.commit.assert_called_once()
    db.refresh.assert_called_once()
    assert author == Author(2, name='Son Goku')


def test_get_all_authors_should_succeed(mocker):
    db = mocker.MagicMock()
    mocked_authors = [Author(1, 'Euclides da Cunha'), Author(2, 'Graciliano Ramos')]
    mocker.patch.object(repository.AuthorRepository, 'list', return_value=mocked_authors)
    assert views.get_authors(db) == mocked_authors


def test_get_book_should_succeed(mocker, some_books):
    db = mocker.MagicMock()
    mocker.patch.object(repository.BookRepository, 'get', return_value=some_books[0])
    assert views.get_book(db, 1) == some_books[0]


def test_get_book_should_raise_error(mocker):
    db = mocker.MagicMock()
    mocker.patch.object(repository.BookRepository, 'get', return_value=None)
    with pytest.raises(HTTPException):
        views.get_book(db, 1)
