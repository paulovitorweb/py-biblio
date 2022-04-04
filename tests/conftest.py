import pytest
from src.pybiblio.orm import InMemorySession, in_memory_engine, metadata


@pytest.fixture
def session():
    metadata.create_all(in_memory_engine)
    yield InMemorySession()
    metadata.drop_all(in_memory_engine)
