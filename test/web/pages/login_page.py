from playwright.sync_api import Page
from test.web.pages.page_base import PageBase

class LoginPage(PageBase):
    def __init__(self, page: Page) -> None:
        super().__init__(page, 
        elements={            
            #"username":  "#username",
            #"password": "#password",
            "login": "#login",
            "register":  "#register",
            #"usernameRegister":  "#username",
            "password1":  "#password1",
            "password2":  "#password2",
            #"registerSuccess":  "#register",

            

        })

    def login(self, username, password):
        self.page.locator("#username:visible").wait_for(state="visible", timeout=10000)
        self.page.locator("#username:visible").fill(username)
        self.page.locator("#password:visible").fill(password)
        self.page.locator("#login:visible").click()

    def click_register(self):
        #self.element("register").click()
        self.page.locator("#register:visible").click()
        self.page.locator("#username:visible").wait_for(state="visible", timeout=10000)
       


    def register(self, username, password, confirm_password):
        self.page.locator("#username:visible").fill(username)
        self.page.locator("#password1:visible").fill(password)
        self.page.locator("#password2:visible").fill(confirm_password)
        self.page.locator("#register:visible").click()

        self.page.locator("#username:visible").wait_for(state="visible", timeout=10000)

        

    

