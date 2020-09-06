from utils.FindLocator import *
from .PageBase import PageBase
from .ProfileManagement import ProfileManagement
class PropertyHomePage(PageBase):

    def __init__(self,driver):
        super().__init__(driver)
        self._allelements=dict()

    @FindBy(how='xpath',locator='//a[contains(text(),"Intel")]',name='Intel Button')
    def intel_button(self):
        return self._allelements['Intel Button']

    @FindBy(how='xpath',locator='//li[a[text()="Intel"]]/ul/li/a[text()="Accounts"]',name='Accounts_1')
    def accounts1(self):
        return self._allelements['Accounts_1']

    @FindBy(how='xpath',locator='//li[a[text()="Accounts"]]/ul/li/a[text()="Accounts"]',name='Accounts_2')
    def accounts2(self):
        return self._allelements['Accounts_2']

    def navigate_to_account_intel(self):
        self.intel_button().click()
        self.accounts1().click()
        self.accounts2().click()
        return ProfileManagement(self.driver)
