from main import add


def test_none():
    assert add(None) is None


def test_empty():
    assert add("") == 0
