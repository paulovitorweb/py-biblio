import pytest
from fastapi import HTTPException
from src.pybiblio.infrastructure import repository
from src.pybiblio.domain.models import Author
from src.pybiblio.api import views


def test_get_author_should_succeed(mocker):
    db = mocker.MagicMock()
    mocker.patch.object(repository.AuthorRepository, 'get', return_value=Author(1, 'Paulo Freitas'))
    assert views.get_author(db, 1) == Author(1, 'Paulo Freitas')


def test_get_author_should_raise_error(mocker):
    db = mocker.MagicMock()
    mocker.patch.object(repository.AuthorRepository, 'get', return_value=None)
    with pytest.raises(HTTPException):
        views.get_author(db, 1)
