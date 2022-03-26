from main import add


def test_none():
    assert add(None) is None


def test_empty():
    assert add("") == 0


def test_single():
    assert add("1") == 1
    assert add("345") == 345


def test_comma():
    assert add("3,2") == 5
    assert add("0,2") == 2
    assert add("0,2,2,6,5,10") == 25


def test_newline():
    assert add("3\n2") == 5
    assert add("0\n2\n7") == 9


def test_comma_newline():
    assert add("3\n2,3") == 8
    assert add("0,2\n5\n3,10") == 20


def test_custom_delimiter():
    assert add("//;\n1;2") == 3
    assert add("//?\n1?9?1") == 11
