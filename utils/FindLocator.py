from utils.LogInitilizer import LogInitilizer
logger=LogInitilizer.getLogger()


class ElementsMeta:
    __instance = False
    __element=None

    @staticmethod
    def getElements():
        if not ElementsMeta.__instance:
            ElementsMeta.__element=dict()
            ElementsMeta.__instance=True
        return ElementsMeta.__element

    @staticmethod
    def addElement(element,name):
        if not ElementsMeta.__instance:
            ElementsMeta.getElements()

        if ElementsMeta.__instance:
            ElementsMeta.__element[element]=name


def FindBy(how, locator, name):
    def real_decorator(method):
        def method_wrapper(self,*args,**kwargs):
            element=create_webelement(self.driver, how, locator,args)
            self._allelements[name]=element
            ElementsMeta.addElement(element.wrapped_element,name)
            return method(self,*args,**kwargs)
        return method_wrapper
    return real_decorator

def FindBys(how, locator, name):
    def real_decorator(method):
        def method_wrapper(self,*args,**kwargs):
            element=create_webelements(self.driver, how, locator,args)
            self._allelements[name]=element
            ElementsMeta.addElement(element[0],name)
            return method(self,*args,**kwargs)
        return method_wrapper
    return real_decorator

def create_webelements(driver,how,some_locator,*args):
    locator = some_locator

    if 'replace_name' in locator:
        to_be_replaced=list(args)[0]
        locator=some_locator.replace('replace_name',to_be_replaced[0])

    if how=='xpath':
        return driver.find_elements_by_xpath(locator)
    if how=='css':
        return driver.find_elements_by_css_selector(locator)
    if how=='id':
        return driver.find_elements_by_id(locator)



def create_webelement(driver,how,some_locator,*args):
    locator=some_locator

    if 'replace_name' in locator:
        to_be_replaced=list(args)[0]
        locator=some_locator.replace('replace_name',to_be_replaced[0])

    if how=='xpath':
        return driver.find_element_by_xpath(locator)
    if how=='css':
        return driver.find_element_by_css_selector(locator)
    if how=='id':
        return driver.find_element_by_id(locator)
    if how=='linktext':
        return driver.find_element_by_link_text(locator)


