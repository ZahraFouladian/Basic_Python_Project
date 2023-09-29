from bank import value


def test_hello_or_h():
    assert value("HELLO") == 0
    assert value("hello") == 0
    assert value("hello zahra") == 0
    assert value("hello, iran") == 0
    assert value("hello, world") == 0
    assert value("Heeeey") == 20
    assert value("heeeeey") == 20
    assert value("hoooooo") == 20
    assert value("how you doing") == 20
    assert value("heello baby") == 20


def test_non_h():
    assert value("salam") == 100
    assert value("what are you doing") == 100
