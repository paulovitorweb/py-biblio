from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import mapper, sessionmaker, relationship
from sqlalchemy.pool import StaticPool
from . import models

in_memory_engine = create_engine(
    'sqlite://', 
    connect_args={'check_same_thread': False}, 
    poolclass=StaticPool
)

InMemorySession = sessionmaker(bind=in_memory_engine)

metadata = MetaData()

author = Table('authors', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(128))
)

association_book_authors = Table('book_authors', metadata,
    Column('book_id', ForeignKey('books.id')),
    Column('author_id', ForeignKey('authors.id'))
)

book = Table('books', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(256)),
    Column('year', Integer),
    Column('location', String(64)),
    Column('publishing_company', String(64))
)

mapper(models.Author, author, properties={
    'books': relationship(models.Book, secondary=association_book_authors, back_populates='authors')
})

mapper(models.Book, book, properties={
    'authors': relationship(models.Author, secondary=association_book_authors, back_populates='books')
})
