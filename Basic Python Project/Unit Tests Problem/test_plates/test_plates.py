from plates import is_valid


def test_invalid():
    assert is_valid("gt%?") == False
    assert is_valid("he llo") == False


def test_length():
    assert is_valid("A") == False
    assert is_valid("asdf1234") == False
    assert is_valid("AB") == True
    assert is_valid("ABC123") == True


def test_start():
    assert is_valid("a12345") == False
    assert is_valid("123ABC") == False
    assert is_valid("8a") == False
    assert is_valid("d5") == False
    assert is_valid("ac") == True


def test_end():
    assert is_valid("avf25n") == False
    assert is_valid("g859le") == False
    assert is_valid("fg123f") == False
    assert is_valid("asd789") == True


def test_length():
    assert is_valid("A") == False
    assert is_valid("asdf1234") == False
    assert is_valid("AB") == True
    assert is_valid("ABC123") == True

def test_zero():
    assert is_valid("gt025") == False
    assert is_valid("he540") == True