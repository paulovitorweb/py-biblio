from sqlalchemy import Table, MetaData, Column, Integer, String, create_engine
from sqlalchemy.orm import mapper, sessionmaker
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

mapper(models.Author, author)
