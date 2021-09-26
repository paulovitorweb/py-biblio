from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


@dataclass
class Author(Base):
    id: int
    full_name: str
    citation_name: str

    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    full_name = Column(String(60))
    citation_name = Column(String(60))

    def __init__(self, full_name: str, citation_name: str = None):
        self.full_name = full_name
        self.citation_name = citation_name or self._make_citation_name()

    def __repr__(self):
        return f'<Author {self.citation_name}>'

    def _make_citation_name(self) -> str:
        items = self.full_name.split()

        last_item = items.pop()
        items_str = ' '.join(items)

        return f'{last_item.upper()}, {items_str}'


@dataclass
class Reference(Base):
    id: int
    title: str
    author: Author

    __tablename__ = 'references'

    id = Column(Integer, primary_key=True)
    title = Column(String(256))
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship('Author', back_populates='references')

    def __init__(self, title: str):
        self.title = title

    def __repr__(self):
        return f'<Reference {self.title}>'


Author.references = relationship(
    "Reference", order_by=Reference.id, back_populates="author"
)
