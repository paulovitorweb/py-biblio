from src.pybiblio.models import Author


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


def test_author_mapper_can_save_authors(session):
    new_author = Author(name='Paulo de Freitas')
    session.add(new_author)
    session.commit()
    rows = list(session.execute('SELECT id, name FROM "authors"'))
    assert rows == [(1, 'Paulo de Freitas')]