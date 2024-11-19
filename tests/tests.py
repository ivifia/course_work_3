from src.func import card,check, executed
import pytest



def test_card():
    assert card('6831982476737658') == '6831 98** **** 7658'
    assert card('5999414228426353') == '5999 41** **** 6353'

def test_check():
    assert check('Счет 72082042523231456215') == '**6215'
    assert check('Счет 72731966109147704472') == '**4472'



def test_executed():
    assert executed()[0]["date"]=="2019-12-08T22:46:21.935582"
    assert executed()[1]["date"]=="2019-12-07T06:17:14.634890"
    assert executed()[-1]["date"]=="2019-11-05T12:04:13.781725"
    for i in range(5):
        assert executed()[i]["state"]=="EXECUTED"