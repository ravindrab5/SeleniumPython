from selenium import webdriver
from utils.LogInitilizer import LogInitilizer
from utils.FindLocator import *
from pages.ManagementCompanyListing import ManagementCompanyListing
from .PageBase import PageBase
logger=LogInitilizer.getLogger()

class LoginPage(PageBase):

    def __init__(self,driver):
        super().__init__(driver)
        self._allelements=dict()

    @FindBy(how='id', locator='username', name='username')
    def username(self):
        return self._allelements.get('username')

    @FindBy(how='id', locator='password', name='password')
    def password(self):
        return self._allelements.get('password')

    @FindBy(how='css', locator="#loginform input[value='Login']", name='login_btn')
    def login_btn(self):
        return self._allelements.get('login_btn')

    def login_with(self,username,password):
        self.username().send_keys(username)
        self.password().send_keys(password)
        self.login_btn().click()
        return ManagementCompanyListing(self.driver)




