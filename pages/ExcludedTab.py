
from .PageBase import PageBase
from utils.FindLocator import FindBy
from utils.FindLocator import FindBys
from .ProfileManagement import ProfileManagement

class ExcludedTab(PageBase):

    def __init__(self,driver):
        super().__init__(driver)
        self._allelements = dict()


    @FindBys(how='xpath',locator="//th[contains(@class,'is-fixed-left')]",name='Grid Header')
    def __grid_header(self):
        return self._allelements['Grid Header']

    @FindBy(how='css',locator='.btn-profile-search',name='Profile Search Popup')
    def __profile_display_popup(self):
        return self._allelements['Profile Search Popup']

    @FindBy(how='xpath',locator="//div[@class='sub-profiles-checkbox checkoption ']/small",name='Sub profile checkbox label')
    def __sub_profile_checkbox_label(self):
        return self._allelements['Sub profile checkbox label']

    @FindBy(how='css',locator='.sub-profiles-checkbox span',name='Sub profile checkbox')
    def __sub_profile_checkbox(self):
        return self._allelements['Sub profile checkbox']

    @FindBy(how='xpath',locator="//span[text()='Select Profile Name']",name='Search button dropdown')
    def __profile_search_button_dropdown(self):
        return self._allelements['Search button dropdown']

    @FindBy(how='xpath',locator="//input[@placeholder='Search..']",name='Search field')
    def __search_field_in_profile_display(self):
        return self._allelements['Search field']

    @FindBys(how='css',locator='.profile-name-select label',name='Search Results')
    def __search_results(self):
        return self._allelements['Search Results']

    @FindBy(how='id',locator='rnFrom',name='rnFromField')
    def __rn_from_field(self):
        return self._allelements['rnFromField']

    @FindBy(how='id',locator='rnTo',name='rnTofield')
    def __rn_to_field(self):
        return self._allelements['rnTofield']

    @FindBy(how='css',locator='.chi-go',name='go button')
    def __go_button(self):
        return self._allelements['go button']


    @FindBy(how='css',locator='.errorAlertPosition strong',name='error text')
    def __error_text(self):
        return self._allelements['error text']

    @FindBys(how='xpath',locator='//tbody/tr/td[3]/span',name='Master Profiles')
    def __list_of_masterProfiles(self):
        return self._allelements['Master Profiles']

    @FindBy(how='css', locator='.chi-edit', name='Edit icon')
    def __edit_icon(self):
        return self._allelements['Edit icon']

    @FindBy(how='css', locator='.chi-save', name='Save Button')
    def __save_button(self):
        return self._allelements['Save Button']

    @FindBy(how='css', locator='tr .chi-close3', name='Cancel Save Button')
    def __cancel_save_button(self):
        return self._allelements['Cancel Save Button']

    @FindBy(how='linktext',locator='Profile Management',name='Profile Management')
    def __profile_management_tab(self):
        return self._allelements['Profile Management']

    @FindBy(how='xpath',locator="//div[@id='globalConfirmationBox']/div/div/div/p",name='No Data popup')
    def __no_data_popup(self):
        return self._allelements['No Data popup']

    @FindBy(how='xpath',locator="//button[text()='OK']",name='Ok button in popup')
    def __ok_button(self):
        return self._allelements['Ok button in popup']

    @FindBy(how='css',locator='table .chi-star',name='Reactivate star icon')
    def __reactivate_icon(self):
        return self._allelements['Reactivate star icon']

    @FindBy(how='css',locator='.dialog-popup-for-excluded-profiles-tab .btn-accept',name='Accept all button')
    def __accept_all_button(self):
        return self._allelements['Accept all button']

    @FindBy(how='css',locator='.dialog-popup-for-excluded-profiles-tab .chi-close3',name='Close button star icon popup')
    def __close_button_star_icon(self):
        return self._allelements['Close button star icon popup']

    @FindBy(how='css',locator='.dialog-popup-for-excluded-profiles-tab .btn-reset',name='Button Reset')
    def __reset_button(self):
        return self._allelements['Button Reset']

    def click_sub_profile_checkbox(self):
        self.__sub_profile_checkbox().click()

    def click_reset_button(self):
        self.__reset_button().click()

    def click_star_reactive_icon(self):
        self.__reactivate_icon().click()

    def is_reset_button_enabled(self):
        return 'disabled' in self.__reset_button().get_attribute('class')

    def click_accept_all(self):
        self.__accept_all_button().click()

    def click_close_button_star_icon(self):
        self.__close_button_star_icon().click()

    def open_reactivate_star_icon(self):
        self.__reactivate_icon().click()

    def click_on_profile_management_tab(self):
        self.__profile_management_tab().click()
        return ProfileManagement(self.driver)

    def click_on_edit_icon(self):
        element=self.driver.find_element_by_id('wait')
        self.waitTillElementInVisibility(element)
        self.__edit_icon().click()

    def click_cancel_save_button(self):
        self.__cancel_save_button().click()

    def click_save_button(self):
        self.__save_button().click()

    def activate_account(self,profile):
        path="//tr[td[span[span[text()='"+profile+"']]]]/td[2]/div/div/div/span/i"
        self.driver.find_element_by_xpath(path).click()

    def all_master_profiles(self):
        self.waitTillElementInVisibility(self.driver.find_element_by_id('wait'))
        getTextFn=lambda element:element.text
        return list(map(getTextFn,self.__list_of_masterProfiles()))

    def get_error_text(self):
        return self.__error_text().text

    def click_go_button(self):
        return self.__go_button().click()

    def enter_to_field(self,rnTo):
        self.__rn_to_field().clear()
        self.__rn_to_field().send_keys(rnTo)

    def enter_from_field(self,rnFrom):
        self.__rn_from_field().clear()
        self.__rn_from_field().send_keys(rnFrom)

    def search_profile_get_result_in_profile_display(self,profile_to_search):
        self.__profile_search_button_dropdown().click()
        self.__search_field_in_profile_display().send_keys(profile_to_search)
        search_results = lambda element: element.text
        return list(map(search_results, self.__search_results()))

    def search_profile_and_select(self,profile_to_search):
        self.__profile_search_button_dropdown().click()
        self.__search_field_in_profile_display().send_keys(profile_to_search)
        path="//label[@title='"+profile_to_search+"']"
        self.driver.find_element_by_xpath(path).click()

    def click_profile_display(self):
        self.__profile_display_popup().click()

    def get_subprofile_label(self):
        return self.__sub_profile_checkbox_label().text

    def get_grid_header_text(self):
        grid_header_text = lambda element: element.text
        return list(map(grid_header_text, self.__grid_header()))[1:]

    def get_profile_display_text(self):
        return self.__profile_display_popup().text

    def is_profile_display_enabled(self):
        return self.__profile_display_popup().is_enabled()

    def is_profile_excluded(self,profilename):
        return 'chi-import-status-red' in self.driver.find_element_by_xpath("//tr[td[span[span[text()='"+profilename+"']]]]/td[2]/div/div/div/span/a/i").get_attribute('class')

    def is_profile_approved(self,profilename):
        return 'chi-approval' in self.driver.find_element_by_xpath("//tr[td[span[span[text()='"+profilename+"']]]]/td[2]/div/div/div/span/i").get_attribute('class')














