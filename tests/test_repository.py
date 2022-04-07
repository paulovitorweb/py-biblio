from src.pybiblio.domain import models
from src.pybiblio.infrastructure import repository


def test_repository_can_save_an_author(session):
    author = models.Author(name='Paulo de Freitas')

    repo = repository.AuthorRepository(session)
    repo.add(author)
    session.commit()

    rows = session.execute(
        'SELECT id, name FROM "authors"'
    )
    assert list(rows) == [(1, 'Paulo de Freitas')]


def test_repository_can_retrieve_an_author(session):
    session.execute(
        'INSERT INTO authors (name) VALUES '
        '("Paulo Freire"),'
        '("Alexandre de Castro")'
    )
    repo = repository.AuthorRepository(session)
    author = repo.get(1)
    assert author == models.Author(1, 'Paulo Freire')


def test_repository_can_retrieve_all_authors(session):
    session.execute(
        'INSERT INTO authors (name) VALUES '
        '("José Augusto da Silveira"),'
        '("Alexandre de Castro")'
    )
    repo = repository.AuthorRepository(session)
    expected = [
        models.Author(1, 'José Augusto da Silveira'), 
        models.Author(2, 'Alexandre de Castro')
    ]
    assert repo.list() == expected


def test_repository_can_save_a_book(session):
    session.execute(
        'INSERT INTO authors (name) VALUES '
        '("Roberto Campagni")'
    )
    book = models.Book(None, 'Economia urbana', 2005, [repository.AuthorRepository(session).get(1)], 'Barcelona', 'Ed. Antonio Bosch')

    repo = repository.BookRepository(session)
    repo.add(book)
    session.commit()

    rows_books = session.execute('SELECT * FROM "books"')
    assert list(rows_books) == [(1, 'Economia urbana', 2005, 'Barcelona', 'Ed. Antonio Bosch')]

    rows_authors = session.execute('SELECT * FROM "authors"')
    assert list(rows_authors) == [(1, 'Roberto Campagni')]

    rows_relations = session.execute('SELECT * FROM "book_authors"')
    assert list(rows_relations) == [(1, 1)]


def test_repository_can_save_a_book_and_related_authors(session):
    book = models.Book(None, 'Economia urbana', 2005, [models.Author(name='Roberto Campagni')], 'Barcelona', 'Ed. Antonio Bosch')

    repo = repository.BookRepository(session)
    repo.add(book)
    session.commit()

    rows_books = session.execute('SELECT * FROM "books"')
    assert list(rows_books) == [(1, 'Economia urbana', 2005, 'Barcelona', 'Ed. Antonio Bosch')]

    rows_authors = session.execute('SELECT * FROM "authors"')
    assert list(rows_authors) == [(1, 'Roberto Campagni')]

    rows_relations = session.execute('SELECT * FROM "book_authors"')
    assert list(rows_relations) == [(1, 1)]


def test_repository_can_retrieve_a_book(session, some_authors):
    session.execute(
        'INSERT INTO authors (name) VALUES '
        '("Paulo de Freitas"),'
        '("Alexandre de Castro")'
    )
    session.execute(
        'INSERT INTO books (title, year, location, publishing_company) VALUES '
        '("A Rede Urbana", 2016, "João Pessoa", "Wordpress")'
    )
    session.execute('INSERT INTO book_authors (book_id, author_id) VALUES (1, 1), (1, 2)')

    repo = repository.BookRepository(session)
    book = repo.get(1)
    assert book == models.Book(1, 'A Rede Urbana', 2016, some_authors[0:2], 'João Pessoa', 'Wordpress')