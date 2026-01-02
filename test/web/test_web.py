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
    
    def test_register_new_user(self):
        login_page = LoginPage(self.page)

        # first to to to registration form
        login_page.click_register()

        # second fill in registration details
        username = f"user_{int(time.time())}"
        password = "password123"
        login_page.register(username, password, password)


        self.page.screenshot(path="agter_registration.png")
        #self.page.locator("#username:visible").wait_for(state="visible", timeout=10000)


        self.page.screenshot(path="agter_registration.png")
        html = self.page.content()
        with open("debug_after_register.html","w", encoding="utf-8") as f:
            f.write(html)
        # third verify that registration succeded
        login_page.login(username, password)
        expect(CalculatorPage(self.page).element("username")).to_have_text(username)



       
        