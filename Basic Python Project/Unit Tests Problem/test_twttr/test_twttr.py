import twttr
from twttr import shorten

def test_vowel():
    assert shorten('aooei') == ''
    assert shorten('oueaae') == ''


def test_no_change():
    assert shorten('qwrt') == 'qwrt'
    assert shorten('dfgh') == 'dfgh'
    assert shorten('sdf45') == 'sdf45'

def test_capital():
    assert shorten('aAoep') == 'p'
    assert shorten('Iran') == 'rn'
    assert  shorten('APPLE') == 'PPL'


def test_non_alpha():
    assert  shorten('12!@') == '12!@'
    assert  shorten('12!*/@87') == '12!*/@87'