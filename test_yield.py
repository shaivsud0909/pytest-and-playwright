import pytest

@pytest.fixture
def setup():
    print("browser setup started ")
    yield
    print("browser setup closed")

def test_one(setup):
    print("setup function")

def test_two(setup):
    print("setup second function")
    