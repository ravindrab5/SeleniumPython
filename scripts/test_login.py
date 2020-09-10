import time
from pages.LoginPage import LoginPage
from base.TestBase import TestBase
from pages.ExcludedTab import ExcludedTab
import pytest


@pytest.mark.usefixtures('createManagementCompanyData','createAccountIntelData')
class TestLogin(TestBase):
    dataFile='SandboxData.json'


    def test_exclude_profile_and_check_list(self):
        self.driver.get(self.env['url'])
        loginpage=LoginPage(self.driver)
        company_listing=loginpage.login_with(self.env['username'],self.env['password'])
        property_listing=company_listing.search_and_click(self.testdata['managementCompanies'][0]['managementCompanyName'])
        property_home=property_listing.click_on_property(self.testdata['properties'][1]['propertyName'])
        profile_management=property_home.navigate_to_account_intel()
        profile_management.clickEditIcon()
        profile_management.exclude_account('Airbus Group')
        profile_management.click_save_button()
        profile_management.exclude_tab().click()
        excluded_tab =ExcludedTab(self.driver)
        time.sleep(2)
        print(excluded_tab.get_grid_header_text())
        time.sleep(2)

        
        
    # def test_2_login(self):
    #     self.driver.get(self.env['url'])
    #     loginpage=LoginPage(self.driver)
    #     loginpage.login_with(self.env['username'],self.env['password'])
    #
    #     time.sleep(2)



