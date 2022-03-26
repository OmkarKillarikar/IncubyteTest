from main import add


def test_none():
    assert add(None) is None


def test_empty():
    assert add("") == 0


def test_single():
    assert add("1") == 1
    assert add("345") == 345


def test_commas():
    assert add("3,2") == 5
    assert add("0,2") == 2
