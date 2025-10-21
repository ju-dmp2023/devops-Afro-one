from BE.calculator_helper import CalculatorHelper
#from assertpy import assert_that
import pytest
from test_base import BaseTestCalculator


class TestCalculator(BaseTestCalculator):


    #set up before each test
    #def setup_method(self):
     #   self.calculator = CalculatorHelper()

    #teardown after each test
    #def teardown_method(self):
     #   self.calculator= None





    @pytest.mark.parametrize("a,b,expected", [
        (1,1,2),(1,-1,0)
    ])


    def test_add(self,a,b,expected):
        value = self.calculator.add(a,b)
        assert value  == expected 
        #assert_that(value).is_equal_to(3)


    #def test_add_negative(self,a,b,expected):
    #    calculator = CalculatorHelper()
    #    value = calculator.add(1,-1)
    #    assert value  == 0   

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