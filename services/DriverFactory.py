from abc import ABC, abstractstaticmethod, abstractmethod
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class DriverManager:

    @staticmethod
    def get_driver(driver_type):
        if driver_type=='chrome':
            return ChromeDriver().create_driver()



class DriverFactory(ABC):
    selenium_grid_url = "http://mn4qmarenvw001.ideasdev.int:4444/wd/hub"

    @abstractmethod
    def create_driver(self):
        pass


class ChromeDriver(DriverFactory):
    def create_driver(self):
        capabilities=DesiredCapabilities.CHROME.copy()
        capabilities['platform'] = "WINDOWS"
        return webdriver.Remote(desired_capabilities=capabilities,command_executor=DriverFactory.selenium_grid_url)

