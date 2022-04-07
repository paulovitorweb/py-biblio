from dataclasses import dataclass, field
from typing import List, Optional, Tuple, NewType


Pages = NewType('Pages', Tuple[int, int])


@dataclass
class Author:
    id: int = field(default=None)
    name: str = field(default=None)

    def __str__(self):
        return self.reference

    def __eq__(self, other):
        if not isinstance(other, Author):
            return False
        return self.id == other.id and self.name == other.name

    def __hash__(self):
        return hash(str(self.id) + self.name)

    @property
    def citation(self) -> str:
        """Author string as citation"""
        return self.name.strip().split()[-1].upper()

    @property
    def reference(self) -> str:
        """Author string as reference"""
        name, _, last_name = self.name.strip().rpartition(' ')
        return f'{last_name.upper()}, {name}'


@dataclass
class Publication:
    id: int = field(default=None)
    title: str = field(default=None)
    year: int = field(default=None)
    authors: List[Author] = field(default=None)

    def __str__(self):
        return self.reference

    @property
    def citation(self) -> str:
        """Publication string as citation"""
        authors = '; '.join([author.citation for author in self.authors])
        return f'({authors}, {self.year})'

    @property
    def reference(self) -> str:
        """Publication string as reference"""
        return f'{self._authors_for_reference()}. {self.title}, {self.year}.'
    
    def _authors_for_reference(self) -> str:
        return '; '.join([author.reference for author in self.authors])


@dataclass
class Book(Publication):
    location: str = field(default=None)
    publishing_company: str = field(default=None)

    @property
    def reference(self) -> str:
        """Book string as reference"""
        return f'{self._authors_for_reference()}. {self.title}. {self.location}: {self.publishing_company}, {self.year}.'


@dataclass
class Article(Publication):
    journal: str = field(default=None)
    volume: int = field(default=None)
    number: int = field(default=None)
    edition_year: int = field(default=None)
    pages: Optional[Pages] = field(default=None)

    @property
    def reference(self) -> str:
        """Article string as reference"""
        authors = self._authors_for_reference()
        ref = f'{authors}. {self.title}. {self.journal}, Vol. {self.volume}, No. {self.number}, Ano {self.edition_year}, {self.year}.'
        return ref if not self.pages else ref + f' p. {self.pages[0]}-{self.pages[1]}.'
    


@dataclass
class Bibliography:
    publications: List[Publication]

    def as_html(self) -> str:
        """Bibliography as html list"""
        items = ''.join([f'<li>{str(publication)}</li>' for publication in self.publications])
        return '<ul>' + items + '</ul>'

    def get_authors(self) -> List[Author]:
        """Authors in the bibliography, no duplicates"""
        return list(set([author for publication in self.publications for author in publication.authors]))
