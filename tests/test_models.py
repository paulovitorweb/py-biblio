from src.pybiblio.models import Author, Reference


def test_instance_author():
    author = Author('Paulo de Freitas')
    assert author.name == 'Paulo de Freitas'
    assert author.citation == 'FREITAS'
    assert author.reference == 'FREITAS, Paulo de'
    assert str(author) == 'FREITAS, Paulo de'


def test_instance_reference():
    authors = [Author('Paulo de Freitas'), Author('Alexandre de Castro')]
    reference = Reference('A Rede Urbana', 2016, authors)
    assert reference.title == 'A Rede Urbana'
    assert reference.year == 2016
    assert reference.authors == [Author('Paulo de Freitas'), Author('Alexandre de Castro')]
    assert reference.citation == '(FREITAS; CASTRO, 2016)'
    assert reference.reference == 'FREITAS, Paulo de; CASTRO, Alexandre de. A Rede Urbana, 2016.'
    assert str(reference) == 'FREITAS, Paulo de; CASTRO, Alexandre de. A Rede Urbana, 2016.'