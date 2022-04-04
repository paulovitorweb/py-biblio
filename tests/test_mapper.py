from sqlalchemy.orm import Session
from src.pybiblio.models import Author, Book


def test_author_mapper_can_load_authors(session: Session):
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


def test_author_mapper_can_save_authors(session: Session):
    new_author = Author(name='Paulo de Freitas')
    session.add(new_author)
    session.commit()
    rows = list(session.execute('SELECT id, name FROM "authors"'))
    assert rows == [(1, 'Paulo de Freitas')]


def test_author_book_mapper_can_get_relationship(session: Session):
    new_book = Book(None, 'Ecossistema GIS', 2020, [Author(name='Paulo de Freitas')], 'João Pessoa', 'Wordpress')
    session.add(new_book)
    session.commit()

    book = session.query(Book).filter_by(id=1).one()
    assert book.authors == [Author(1, 'Paulo de Freitas')]

    author = session.query(Author).filter_by(id=1).one()
    assert author.books == [book]
