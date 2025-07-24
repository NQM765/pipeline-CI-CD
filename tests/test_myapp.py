# tests/test_myapp.py
from myapp import hello

def test_hello():
    assert hello() == "Hello, World!"
