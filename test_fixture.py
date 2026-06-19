import pytest

@pytest.fixture
def setup():
    print("browser setup")
    return "chrome"

def test_one(setup):
    print("setup function")
    print(setup)

def test_two(setup):
    print("setup second function")
    