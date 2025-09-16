from BE.calculator_helper import CalculatorHelper


class BaseTestCalculator:
     #set up before each test
    def setup_method(self):
        self.calculator = CalculatorHelper()

    #teardown after each test
    def teardown_method(self):
        self.calculator = None