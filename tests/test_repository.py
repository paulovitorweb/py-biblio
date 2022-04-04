from src.pybiblio import models
from src.pybiblio import repository


def test_repository_can_save_a_author(session):
    author = models.Author(name='Paulo de Freitas')

    repo = repository.AuthorRepository(session)
    repo.add(author)
    session.commit()

    rows = session.execute(
        'SELECT id, name FROM "authors"'
    )
    assert list(rows) == [(1, 'Paulo de Freitas')]