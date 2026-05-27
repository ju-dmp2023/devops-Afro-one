from test.web.test_base import WebBase
from test.web.pages.login_page import LoginPage
from test.web.pages.calculator_page import CalculatorPage
from test.web.pages.register_page import RegisterPage
from playwright.sync_api import expect
import pytest
import time
#import random

class TestWeb(WebBase):
    def test_login(self):
        LoginPage(self.page).login(username="admin", password="test1234")
        expect(CalculatorPage(self.page).element("username")).to_have_text("admin")
        CalculatorPage(self.page).element("logout").click()

    def test_register_new_user(self):
        LoginPage(self.page).element("register").click()
        username = f"user_{int(time.time())}"
        password = "password123"
        RegisterPage(self.page).register_user(username, password)
        expect(CalculatorPage(self.page).element("username")).to_have_text(username, timeout=10000)
        CalculatorPage(self.page).element("logout").click()

    def test_add(self):
        LoginPage(self.page).login(username="admin", password="test1234")
        number1 = "1"
        number2 = "2"
        result = "3"
        CalculatorPage(self.page).calculate(number1, "+", number2)
        expect(CalculatorPage(self.page).element("screen")).to_have_value(result)
        CalculatorPage(self.page).element("logout").click()
