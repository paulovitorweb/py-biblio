from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, types, create_engine
from sqlalchemy.orm import mapper, sessionmaker, relationship, Session
from sqlalchemy.pool import StaticPool
from ..domain import models


class Pages(types.TypeDecorator):
    impl = types.String

    def process_bind_param(self, value, dialect):
        if value:
            return f'{value[0]},{value[1]}'

    def process_result_value(self, value, dialect):
        if value:
            start, end = value.split(',')
            return int(start), int(end)


# Db for tests
in_memory_engine = create_engine(
    'sqlite://', connect_args={'check_same_thread': False}, poolclass=StaticPool
)
InMemorySession = sessionmaker(bind=in_memory_engine)


engine = create_engine('sqlite:///database.db', connect_args={'check_same_thread': False})
DbSession = sessionmaker(bind=engine)


metadata = MetaData()

author = Table(
    'authors',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(128)),
)

association_book_authors = Table(
    'book_authors',
    metadata,
    Column('book_id', ForeignKey('books.id')),
    Column('author_id', ForeignKey('authors.id')),
)

book = Table(
    'books',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(256)),
    Column('year', Integer),
    Column('location', String(64)),
    Column('publishing_company', String(64)),
)

association_article_authors = Table(
    'article_authors',
    metadata,
    Column('article_id', ForeignKey('articles.id')),
    Column('author_id', ForeignKey('authors.id')),
)

article = Table(
    'articles',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(256)),
    Column('year', Integer),
    Column('journal', String(64)),
    Column('volume', Integer),
    Column('number', Integer),
    Column('edition_year', Integer),
    Column('pages', Pages),
)

mapper(
    models.Author,
    author,
    properties={
        'books': relationship(
            models.Book, secondary=association_book_authors, back_populates='authors'
        ),
        'articles': relationship(
            models.Article, secondary=association_article_authors, back_populates='authors'
        ),
    },
)

mapper(
    models.Book,
    book,
    properties={
        'authors': relationship(
            models.Author, secondary=association_book_authors, back_populates='books'
        )
    },
)

mapper(
    models.Article,
    article,
    properties={
        'authors': relationship(
            models.Author, secondary=association_article_authors, back_populates='articles'
        )
    },
)


def init_db():
    metadata.create_all(engine)
