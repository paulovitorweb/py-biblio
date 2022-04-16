from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.pybiblio.infrastructure.orm import metadata
from src.pybiblio.api.main import app, get_db

SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


class TestContext:
    author_id: int
    author_obj: dict
    book_id: int


context = TestContext()


def test_api_create_author():
    response = client.post(
        '/authors/',
        json={'name': 'Cecília Meireles'},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['name'] == 'Cecília Meireles'
    assert data['citation'] == 'MEIRELES'
    assert data['reference'] == 'MEIRELES, Cecília'
    assert 'id' in data
    context.author_id = data['id']
    context.author_obj = data


def test_api_create_author_with_invalid_payload():
    response = client.post(
        '/authors/',
        json={'author': 'Missing name'},
    )
    assert response.status_code == 422


def test_api_get_author():
    response = client.get(f'/authors/{context.author_id}')
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['id'] == context.author_id
    assert data['name'] == 'Cecília Meireles'
    assert data['citation'] == 'MEIRELES'
    assert data['reference'] == 'MEIRELES, Cecília'


def test_api_get_author_with_invalid_id():
    response = client.get(f'/authors/0')
    assert response.status_code == 404


def test_api_create_book():
    response = client.post(
        '/books/',
        json={
            'title': 'Janela Mágica',
            'year': 2018,
            'publishing_company': 'Editora Global',
            'location': 'São Paulo',
            'authors': [context.author_id],
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['title'] == 'Janela Mágica'
    assert data['year'] == 2018
    assert data['publishing_company'] == 'Editora Global'
    assert data['location'] == 'São Paulo'
    assert data['authors'] == [context.author_obj]
    assert data['citation'] == '(MEIRELES, 2018)'
    assert data['reference'] == 'MEIRELES, Cecília. Janela Mágica. São Paulo: Editora Global, 2018.'
    assert 'id' in data
    context.book_id = data['id']
