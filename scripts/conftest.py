import pytest
from utils.EventListener import EventListener
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from services.DriverFactory import *
from utils.Environment import Environment
from utils.DataLoader import DataLoader
from utils.LogInitilizer import LogInitilizer
logger=LogInitilizer.getLogger()
env=None

def pytest_addoption(parser):
    parser.addoption("--en", action="store", help="my option: type1 or type2")


def pytest_generate_tests(metafunc):
    env_str=metafunc.config.getoption("en")
    global env
    env= Environment.get_environment(env_str)

@pytest.yield_fixture
def driver(request):
    temp_driver=DriverManager.get_driver('chrome')
    temp_driver.maximize_window()
    temp_driver.implicitly_wait(30)
    driver=EventFiringWebDriver(temp_driver, EventListener())
    if request.cls is not None:
        request.cls.driver=driver
    yield driver
    driver.quit()

@pytest.yield_fixture
def env_setup(request):
    print(request.function.__name__)
    global env
    if request.cls is not None:
        request.cls.env=env
    yield env


@pytest.fixture(scope='class',autouse=True)
def createManagementCompanyData(request):
    logger.info("Creating management company Data")
    dataloader = DataLoader(request.cls.dataFile,env)
    dataloader.deleteManagementAndPropertySetup()
    dataloader.createManagementAndProperty()
    request.cls.testdata = dataloader.getData()

@pytest.fixture(autouse=True)
def createAccountIntelData(request):
    logger.info("Creating Module level data")
    dataloader = DataLoader(request.cls.dataFile, env)
    dataloader.deleteAccountIntelData()
    dataloader.createAccountIntelData()



