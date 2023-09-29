
from seasons import days_diffrence

def test_days_diffrence():
    assert days_diffrence('1995-01-01') == "Fifteen milion, one hundred nine thousand, nine hundred twenty minutes"
    assert days_diffrence('um') == False
    assert days_diffrence('January 1, 1999') == False
    assert days_diffrence('2021-09-24') == "Five hundred twenty-five thousand, six hundred minutes"
    assert days_diffrence('2022-09-24') == "One million, fifty-one thousand, two hundred minutes"

