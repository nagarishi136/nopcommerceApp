import pytest
from selenium import  webdriver
from webdriver_manager.firefox import GeckoDriverManager
#from webdriver_manager.chrome import

from Config.config import TestData


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
       driver=webdriver.Chrome()
       print("Lanuching chrome browser ------")
       #return driver
    elif browser == "fireFox":
        driver=webdriver.firefox(executable_path=GeckoDriverManager().install())
        print("Lanuching firefox browser ------")
        return driver
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")




def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def broswer(request):
   return  request.config.getoption("--browser")
""" ****************** HTML REPORTS """
def pytest_configure(config):
    config._metadata['Project Name']= 'POMDemo'
    config._metadata['Module Name'] ='customers'
    config._metadata['Tester']='Naga'
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Java Home",None)