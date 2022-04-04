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


def test_repository_can_retrieve_a_author(session):
    session.execute(
        'INSERT INTO authors (name) VALUES '
        '("Paulo de Freitas"),'
        '("Alexandre de Castro")'
    )
    repo = repository.AuthorRepository(session)
    author = repo.get(1)
    assert author == models.Author(1, 'Paulo de Freitas')


def test_repository_can_retrieve_all_authors(session):
    session.execute(
        'INSERT INTO authors (name) VALUES '
        '("Paulo de Freitas"),'
        '("Alexandre de Castro")'
    )
    repo = repository.AuthorRepository(session)
    expected = [
        models.Author(1, 'Paulo de Freitas'), 
        models.Author(2, 'Alexandre de Castro')
    ]
    assert repo.list() == expected