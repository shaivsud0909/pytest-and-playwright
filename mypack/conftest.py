import pytest

@pytest.fixture()
def setup():
    print("setup enviornment")
    yield
    print("tearDown...")

# python -m pytest mypack  -s -v

# pytest mypack -m smoke 