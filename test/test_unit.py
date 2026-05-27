from BE.calculator_helper import CalculatorHelper
import pytest
from test.test_base import BaseTestCalculator

class TestCalculator(BaseTestCalculator):

    @pytest.mark.parametrize("a,b,expected", [
        (1,1,2),(1,-1,0)
    ])
    def test_add(self,a,b,expected):
        value = self.calculator.add(a,b)
        assert value  == expected 

    def test_add_negative(self):
        calculator = CalculatorHelper()
        value = calculator.add(1,-1)
        assert value  == 0

    def test_subtract(self):
        value = self.calculator.subtract(1,1)
        assert value  == 0

    def test_multiply(self):
        value = self.calculator.multiply(1,-1)
        assert value  == -1 

    def test_divide(self):
        value = self.calculator.divide(1,-1)
        assert value  == -1

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calculator.divide(1,0)