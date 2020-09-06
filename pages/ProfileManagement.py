from utils.FindLocator import FindBy
from .PageBase import PageBase
# from .ExcludedTab import ExcludedTab

class ProfileManagement(PageBase):

    def __init__(self,driver):
        super().__init__(driver)
        self._allelements=dict()


    @FindBy(how='xpath',locator="//a[contains(text(),'Excluded Profiles')]",name='Excluded Tab')
    def exclude_tab(self):
        return self._allelements['Excluded Tab']

    @FindBy(how='css',locator='.chi-edit',name='Edit icon')
    def edit_button(self):
        return self._allelements['Edit icon']

    @FindBy(how='css',locator='.chi-save',name='Save Button')
    def save_button(self):
        return self._allelements['Save Button']

    @FindBy(how='css',locator='tr .chi-close3',name='Cancel Save Button')
    def cancel_save_button(self):
        return self._allelements['Cancel Save Button']

    def clickEditIcon(self):
        super().waitTillElementInVisibility(self.driver.find_element_by_id('wait'))
        self.edit_button().click()

    def click_cancel_save(self):
        self.cancel_save_button().click()

    def click_save_button(self):
        self.save_button().click()

    def exclude_account(self,profile):
        path = "//tr[td[span[span[text()='" + profile + "']]]]/td[2]/div/div/div/span/i[contains(@class,'chi-exclude')]"
        self.driver.find_element_by_xpath(path).click()

    # def navigate_to_exclude_tab(self):
    #     self.exclude_tab().click()
    #     return ExcludedTab(self.driver)

    def is_profile_pending(self,profile):
        path="//tr[td[span[span[text()='"+profile+"']]]]/td[2]/div/div/div/span/a/i"
        return 'chi-pending' in self.driver.find_element_by_xpath(path).get_attribute("class")

    def is_profile_accepted(self,profile):
        path = "//tr[td[span[span[text()='"+profile+"']]]]/td[2]/div/div/div/span/a/i"
        return 'chi-approval' in self.driver.find_element_by_xpath(path).get_attribute("class")

    def is_contracted_profile(self,profile):
        path = "//tr[td[span[span[text()='"+profile+"']]]]/td[last()]/div/i"
        return 'chi-tic' in self.driver.find_element_by_xpath(path).get_attribute("class")










