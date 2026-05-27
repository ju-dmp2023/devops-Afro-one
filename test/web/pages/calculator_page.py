from playwright.sync_api import Page
from test.web.pages.page_base import PageBase

class CalculatorPage(PageBase):
    def __init__(self, page: Page) -> None:
        super().__init__(page,
        elements={
            "screen": "#calculator-screen",
            "0":  "#key-0",
            "1":  "#key-1",
            "2":  "#key-2",
            "3":  "#key-3",
            "4":  "#key-4",
            "5":  "#key-5",
            "6":  "#key-6",
            "7":  "#key-7",
            "8":  "#key-8",
            "9":  "#key-9",
            "+":  "#key-add",
            "-": "#key-subtract",
            "*": "#key-multiply",
            "/": "#key-divide",
            ",": "#key-decimal",
            "c": "#key-clear",
            "history": "#toggle-button",
            "history_calculations": "#history",
            "=": "#key-equals",
            "username": "#user-name",
            "logout": "#logout-button"
        })

    def calculate(self, number1, operator, number2):
        pass