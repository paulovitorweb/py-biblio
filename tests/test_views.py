import pytest
from src.pybiblio.models import Author
from src.pybiblio.orm import InMemorySession


@pytest.fixture
def session():
    return InMemorySession()


def test_author_mapper_can_load_authors(session):
    session.execute(
        'INSERT INTO authors (name) VALUES '
        '("Paulo de Freitas"),'
        '("Alexandre de Castro")'
    )
    expected = [
        Author(1, 'Paulo de Freitas'),
        Author(2, 'Alexandre de Castro')
    ]
    assert session.query(Author).all() == expected