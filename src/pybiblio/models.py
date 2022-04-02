from dataclasses import dataclass
from typing import List


@dataclass
class Author:
    id: int
    name: str

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
    id: int
    title: str
    year: int
    authors: List[Author]

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
        authors = '; '.join([author.reference for author in self.authors])
        return f'{authors}. {self.title}, {self.year}.'


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
