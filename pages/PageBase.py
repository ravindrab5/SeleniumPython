from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class PageBase:

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

    def waitTillElementVisible(self,element):
        try:
            self.wait.until(EC.visibility_of_element_located(element))
        finally:
            pass

    def waitTillElementClickable(self,element):
        try:
            self.wait.until(EC.element_to_be_clickable(element))
        finally:
            pass

    def waitTillElementInVisibility(self,element):
        try:
            self.wait.until(EC.invisibility_of_element(element.wrapped_element))
        finally:
            pass


