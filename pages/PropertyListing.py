from utils.FindLocator import *
from pages.PropertyHomePage import PropertyHomePage
from .PageBase import PageBase
class PropertyListing(PageBase):

    def __init__(self,driver):
        super().__init__(driver)
        self._allelements=dict()

    @FindBy(how='xpath',locator="//a[contains(text(),'replace_name')]",name="Property name")
    def property_name_from_listing(self,property_name):
        return self._allelements['Property name']

    def click_on_property(self,property_name):
        self.property_name_from_listing(property_name).click()
        return PropertyHomePage(self.driver)