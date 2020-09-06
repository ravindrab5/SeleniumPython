from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from utils.LogInitilizer import LogInitilizer
from utils.FindLocator import ElementsMeta
logger=LogInitilizer.getLogger()


class EventListener(AbstractEventListener):

    def before_navigate_to(self, url, driver):
        pass

    def after_navigate_to(self, url, driver):
        pass

    def before_navigate_back(self, driver):
        pass

    def after_navigate_back(self, driver):
        pass

    def before_navigate_forward(self, driver):
        pass

    def after_navigate_forward(self, driver):
        pass

    def before_find(self, by, value, driver):
        pass

    def after_find(self, by, value, driver):
        pass

    def before_click(self, element, driver):
        pass

    def after_click(self, element, driver):
        logger.info(f"Clicked on element {ElementsMeta.getElements().get(element)}")

    def before_change_value_of(self, element, driver):
        pass

    def after_change_value_of(self, element, driver):
        logger.info(f"Typed on element {ElementsMeta.getElements().get(element)}")

    def before_execute_script(self, script, driver):
        pass

    def after_execute_script(self, script, driver):
        pass

    def before_close(self, driver):
        pass

    def after_close(self, driver):
        pass

    def before_quit(self, driver):
        pass

    def after_quit(self, driver):
        pass

    def on_exception(self, exception, driver):
        pass
