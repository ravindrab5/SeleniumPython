from utils.FindLocator import *
from pages.PropertyListing import PropertyListing
from .PageBase import PageBase

class ManagementCompanyListing(PageBase):

    def __init__(self,driver):
        super().__init__(driver)
        self._allelements=dict()


    @FindBy(how='css',locator='.search input',name='Search box')
    def search(self):
        return self._allelements['Search box']

    @FindBy(how='xpath',locator='//a[contains(text(),"replace_name")]',name='ManagementCompanyInTable')
    def management_company_in_table(self,name):
        return self._allelements['ManagementCompanyInTable']

    def search_and_click(self,management_company):
        self.search().send_keys(management_company)
        self.management_company_in_table(management_company).click()
        return PropertyListing(self.driver)



