from dataclasses import dataclass
from typing import List


@dataclass
class Author:
    name: str

    def __str__(self):
        return self.reference

    @property
    def citation(self) -> str:
        return self.name.strip().split()[-1].upper()

    @property
    def reference(self) -> str:
        name, _, last_name = self.name.strip().rpartition(' ')
        return f'{last_name.upper()}, {name}'


@dataclass
class Reference:
    title: str
    year: int
    authors: List[Author]

    def __str__(self):
        return self.reference

    @property
    def citation(self) -> str:
        authors = '; '.join([author.citation for author in self.authors])
        return f'({authors}, {self.year})'

    @property
    def reference(self) -> str:
        authors = '; '.join([author.reference for author in self.authors])
        return f'{authors}. {self.title}, {self.year}.'
