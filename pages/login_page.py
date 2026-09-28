import os

from dotenv import load_dotenv
from playwright.sync_api import Page

load_dotenv()


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(os.getenv("BASE_URL"))

    def login(self, username, password):
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()