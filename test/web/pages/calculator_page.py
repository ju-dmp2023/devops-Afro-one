from playwright.sync_api import Page
from test.web.pages.page_base import PageBase

class CalculatorPage(PageBase):
    def __init__(self, page: Page) -> None:
        super().__init__(page, 
        elements={            
            "username":  "#user-name",
            "number1":  "#number1",
            "number2":  "#number2",
            "username":  "#user-name",
            
            

        })

   