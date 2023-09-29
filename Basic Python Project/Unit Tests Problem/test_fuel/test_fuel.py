from fuel import convert, gauge
import pytest

def test_errors_convert():
    with pytest.raises(ValueError):
         convert('6/2')
    with pytest.raises(ZeroDivisionError):
         convert('6/0')

def test_convert():
    assert convert('2/5') == 40
    assert convert('0/1') == 0
    assert convert('10/10') == 100

def test_guage():
    assert gauge(0.2) == 'E'
    assert gauge(1) == 'E'
    assert gauge(0) == 'E'
    assert gauge(99) == 'F'
    assert gauge(99.5) == 'F'
    assert gauge(100) == 'F'
    assert gauge(30) == '30%'