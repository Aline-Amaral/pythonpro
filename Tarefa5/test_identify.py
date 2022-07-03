import pytest
from identify import identify_number

class TestIdentify:
    def setup(self):
        pass

    def test_identify_both(self):
        identifyNumber = identify_number(35)
        result = "fizzbuzz"
        assert identifyNumber == result

    def test_identify_7(self):
        identifyNumber = identify_number(14)
        result = "buzz"
        assert identifyNumber == result

    def test_identify_5(self):
        identifyNumber = identify_number(10)
        result = "fizz"
        assert identifyNumber == result

    def test_identify_none(self):
        identifyNumber = identify_number(9)
        result = "miss"
        assert identifyNumber == result