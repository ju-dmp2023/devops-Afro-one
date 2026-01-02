from test.web.test_base import WebBase
from test.web.pages.login_page import LoginPage
from test.web.pages.calculator_page import CalculatorPage
from playwright.sync_api import expect
import pytest
import time
#import random

class TestWeb(WebBase):
    def test_login(self):
        LoginPage(self.page).login(username="admin", password="test1234")
        expect(CalculatorPage(self.page).element("username")).to_have_text("admin")
        self.page.locator("#logout-button").click()
    
    def test_register_new_user(self):
        login_page = LoginPage(self.page)

        # Go to registration form
        login_page.click_register()

        # Fill in registration details
        username = f"user_{int(time.time())}"
        password = "password123"
        login_page.register(username, password, password)

        # Verify registration succeeded
        expect(CalculatorPage(self.page).element("username")).to_have_text(username)

        # Log out
        self.page.locator("#logout-button").click()


       
        