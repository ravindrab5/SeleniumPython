import time
from pages.LoginPage import LoginPage
from base.TestBase import TestBase
from pages.ExcludedTab import ExcludedTab
from pages.ProfileManagement import ProfileManagement
import pytest


@pytest.mark.usefixtures('createManagementCompanyData','createAccountIntelData')
class TestExcludedTab(TestBase):
    dataFile='SandboxData.json'

    def navigateToAccountIntel(self):
        self.driver.get(self.env['url'])
        loginpage = LoginPage(self.driver)
        company_listing = loginpage.login_with(self.env['username'], self.env['password'])
        property_listing = company_listing.search_and_click(
        self.testdata['managementCompanies'][0]['managementCompanyName'])
        property_home = property_listing.click_on_property(self.testdata['properties'][1]['propertyName'])
        profile_management = property_home.navigate_to_account_intel()


    def test_profile_name_search_in_profile_display(self):
        self.navigateToAccountIntel()
        profile_management=ProfileManagement(self.driver)
        profile_management.exclude_tab().click()
        excluded_tab=ExcludedTab(self.driver)
        excluded_tab.click_profile_display()
        actual=excluded_tab.search_profile_get_result_in_profile_display('Kuoni Group')
        expected=['All Profiles','Kuoni Group']
        assert actual==expected

        self.driver.refresh()
        excluded_tab.click_profile_display()
        actual = excluded_tab.search_profile_get_result_in_profile_display('*Lego')
        assert actual == expected

        self.driver.refresh()
        excluded_tab.click_profile_display()
        actual = excluded_tab.search_profile_get_result_in_profile_display('*gover')
        expected=["All Profiles","Norwegian Government"]
        assert actual == expected

        self.driver.refresh()
        excluded_tab.click_profile_display()
        actual = excluded_tab.search_profile_get_result_in_profile_display('asdfsa')
        expected = ['No result found']
        assert actual == expected


    def test_rn_filter_invalid_data(self):
        self.navigateToAccountIntel()
        profile_management = ProfileManagement(self.driver)
        profile_management.exclude_tab().click()
        excluded_tab = ExcludedTab(self.driver)
        excluded_tab.click_profile_display()
        excluded_tab.enter_to_field('-5')
        excluded_tab.click_go_button()
        actual=excluded_tab.get_error_text()
        expected='Please enter valid RN (To) number.'
        assert actual == expected

        self.driver.refresh()
        excluded_tab.click_profile_display()
        excluded_tab.enter_from_field('-5')
        excluded_tab.click_go_button()
        actual = excluded_tab.get_error_text()
        expected = 'Please enter valid RN (from) number.'
        assert actual == expected

        self.driver.refresh()
        excluded_tab.click_profile_display()
        excluded_tab.enter_to_field('1')
        excluded_tab.enter_from_field('5')
        excluded_tab.click_go_button()
        actual = excluded_tab.get_error_text()
        expected='To value must be greater than from value.'
        assert actual == expected

    def test_grid_creation_based_on_valid_rn_filters(self):
        self.navigateToAccountIntel()
        profile_management = ProfileManagement(self.driver)
        profile_management.exclude_tab().click()
        excluded_tab = ExcludedTab(self.driver)
        excluded_tab.click_profile_display()
        excluded_tab.enter_from_field('2')
        excluded_tab.enter_to_field('5')
        excluded_tab.click_go_button()

        actual=excluded_tab.all_master_profiles()
        expected=["New accenture","Norges Fotballforbund","Norwegian Government"]
        assert actual==expected

        self.driver.refresh()
        excluded_tab.click_profile_display()

        excluded_tab.enter_from_field('2')
        excluded_tab.click_go_button()
        actual = excluded_tab.all_master_profiles()
        expected = ["New accenture", "Norges Fotballforbund", "Norwegian Government"]
        assert actual == expected

    def test_profile_name_filter(self):
        self.navigateToAccountIntel()
        profile_management = ProfileManagement(self.driver)
        profile_management.exclude_tab().click()
        excluded_tab = ExcludedTab(self.driver)
        excluded_tab.click_profile_display()
        excluded_tab.search_profile_and_select('Kuoni Group')
        excluded_tab.click_go_button()
        actual=excluded_tab.all_master_profiles()
        expected=["Kuoni Group"]

        assert actual==expected

    def test_single_multiple_profile_activate(self):
        self.navigateToAccountIntel()
        profile_management = ProfileManagement(self.driver)
        profile_management.exclude_tab().click()
        excluded_tab = ExcludedTab(self.driver)
        excluded_tab.click_on_edit_icon()
        excluded_tab.activate_account('Kuoni Group')
        excluded_tab.activate_account('Norwegian Government')
        excluded_tab.click_save_button()

        actual=excluded_tab.all_master_profiles()
        expected=["New accenture","Norges Fotballforbund"]
        assert actual==expected

        excluded_tab.click_on_profile_management_tab()
        assert True == profile_management.is_profile_accepted('Kuoni Group')
        assert True == profile_management.is_profile_accepted('Norwegian Government')

    def test_activate_profile_previously_in_pending_state(self):
        self.navigateToAccountIntel()
        profile_management = ProfileManagement(self.driver)
        profile_management.clickEditIcon()
        profile_management.exclude_account('Airbus Group')
        profile_management.click_save_button()
        profile_management.exclude_tab().click()
        exclude_tab=ExcludedTab(self.driver)
        actual=exclude_tab.all_master_profiles()
        expected=["Airbus Group","Kuoni Group","New accenture","Norges Fotballforbund","Norwegian Government"]
        assert actual==expected

        exclude_tab.click_on_edit_icon()
        exclude_tab.activate_account('Airbus Group')
        exclude_tab.click_save_button()
        actual=exclude_tab.all_master_profiles()
        expected=["Kuoni Group","New accenture","Norges Fotballforbund","Norwegian Government"]
        assert actual ==  expected

        profile_management=exclude_tab.click_on_profile_management_tab()
        assert True == profile_management.is_profile_accepted('Airbus Group')

    def test_contracted_flag_is_set_to_false_when_returned_from_excluded_tab(self):
        self.navigateToAccountIntel()
        profile_management = ProfileManagement(self.driver)
        profile_management.clickEditIcon()
        profile_management.exclude_account('Eli Lilly & Company')
        profile_management.click_save_button()

        profile_management.exclude_tab().click()
        excluded_tab=ExcludedTab(self.driver)

        actual=excluded_tab.all_master_profiles()
        expected=["Eli Lilly & Company","Kuoni Group","New accenture","Norges Fotballforbund","Norwegian Government"]

        assert actual==expected

        excluded_tab.click_on_edit_icon()
        excluded_tab.activate_account('Eli Lilly & Company')
        excluded_tab.click_save_button()
        actual=excluded_tab.all_master_profiles()
        expected=["Kuoni Group","New accenture","Norges Fotballforbund","Norwegian Government"]

        assert actual==expected

        excluded_tab.click_on_profile_management_tab()
        assert True==profile_management.is_profile_accepted('Eli Lilly & Company')
        assert False==profile_management.is_contracted_profile('Eli Lilly & Company')


    def test_profile_list_when_profile_activated_but_changes_not_saved(self):
        self.navigateToAccountIntel()
        profile_management = ProfileManagement(self.driver)
        profile_management.exclude_tab().click()
        excluded_tab=ExcludedTab(self.driver)
        excluded_tab.click_on_edit_icon()
        excluded_tab.activate_account('Kuoni Group')
        excluded_tab.activate_account('Norwegian Government')
        excluded_tab.click_cancel_save_button()
        actual=excluded_tab.all_master_profiles()
        expected=["Kuoni Group","New accenture","Norges Fotballforbund","Norwegian Government"]
        assert actual==expected

    def test_profile_display_icon_disabled_in_edit_mode(self):
        self.navigateToAccountIntel()
        profile_management = ProfileManagement(self.driver)
        profile_management.exclude_tab().click()
        excluded_tab = ExcludedTab(self.driver)
        excluded_tab.click_on_edit_icon()
        assert True==excluded_tab.is_profile_display_enabled()

    def test_reset_button_disabled_when_user_clicks_intially(self):
        self.navigateToAccountIntel()
        profile_management = ProfileManagement(self.driver)
        profile_management.exclude_tab().click()
        excluded_tab = ExcludedTab(self.driver)
        excluded_tab.click_on_edit_icon()
        excluded_tab.click_star_reactive_icon()
        time.sleep(5)
        assert True==excluded_tab.is_reset_button_enabled()
        excluded_tab.click_close_button_star_icon()

    def test_reset_functionality_when_few_marked_accepted(self):
        self.navigateToAccountIntel()
        profile_management = ProfileManagement(self.driver)
        profile_management.exclude_tab().click()
        excluded_tab = ExcludedTab(self.driver)
        excluded_tab.click_on_edit_icon()
        excluded_tab.activate_account('Kuoni Group')
        excluded_tab.activate_account('Norwegian Government')
        assert True == excluded_tab.is_profile_approved('Kuoni Group')
        assert True==excluded_tab.is_profile_approved('Norwegian Government')
        excluded_tab.click_star_reactive_icon()
        excluded_tab.click_reset_button()
        excluded_tab.click_close_button_star_icon()
        excluded_tab.click_cancel_save_button()
        assert True==excluded_tab.is_profile_excluded('Kuoni Group')
        assert True==excluded_tab.is_profile_excluded('Norwegian Government')

    def test_contracted_flag_when_profile_marked_excluded_by_exclude_all_operation(self):
        self.navigateToAccountIntel()
        profile_management = ProfileManagement(self.driver)
        profile_management.clickEditIcon()
        profile_management.exclude_account('Eli Lilly & Company')
        profile_management.click_save_button()

        profile_management.exclude_tab().click()
        excluded_tab = ExcludedTab(self.driver)

        actual=excluded_tab.all_master_profiles()
        expected=["Eli Lilly & Company","Kuoni Group","New accenture","Norges Fotballforbund","Norwegian Government"]

        assert actual==expected

        excluded_tab.click_on_edit_icon()
        excluded_tab.click_star_reactive_icon()
        excluded_tab.click_accept_all()
        excluded_tab.click_close_button_star_icon()
        excluded_tab.click_save_button()

        excluded_tab.click_on_profile_management_tab()
        assert False==profile_management.is_profile_pending('Eli Lilly & Company')
        assert False==profile_management.is_profile_pending('Eli Lilly & Company')