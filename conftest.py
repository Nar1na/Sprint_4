from .main import BooksCollector
import pytest

@pytest.fixture(autouse=True)
def collector():
    return BooksCollector()
