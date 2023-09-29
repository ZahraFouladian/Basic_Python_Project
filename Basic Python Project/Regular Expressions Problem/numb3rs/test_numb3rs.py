from numb3rs import validate


def test_one():
    assert validate("10.142.150.100") == True
    assert validate("200.111.145.22") == True
    assert validate("52..70.") == False
    assert validate("52.15.70.300") == False
    assert validate("-52.15.70.300") == False


def test_two():
    assert validate("cat.001.baby.?") == False
    assert validate("hello") == False
    assert validate("110.85.125") == False
    assert validate("1.15.16.17.87") == False


