"""
__author__= Maria Borisov

"""

# Imports
import pytest
import os
from Utilities import utils
from selenium import webdriver

# Get current directory
current_dir = os.getcwd()


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def browser_setup(request):
    """ Fixture opens Webpage in Chrome and Firefox.
    If fixture is set to "function", all the tests will execute in separate browser sessions.
    :param request: List of Browsers ["chrome", "firefox"]
    :return: driver object
    """
    driver = start_driver(request.param)
    utils.driver = driver
    yield driver  # Suspends execution of the fixture and sends driver value to the test
    driver.close()  # Teardown, executes after test complete. This code will execute no matter of the state of the test


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def browser_login_setup(request):
    """Fixture opens Webpage in Chrome and Firefox and then logs in with valid account.
    If fixture set to "session", all the tests will execute in the same browser session.
    If fixture is set to "function", all the tests will execute in separate browser sessions.
    :param request: List of Browser ["chrome", "firefox"]
    :return: driver object
    """
    driver = start_driver(request.param)
    utils.driver = driver
    utils.helper_functions().login(username="testUser", password="Test1234")
    yield driver  # Suspends execution of the fixture and sends driver value to the test
    driver.close()  # Teardown, executes after test complete. This code will execute no matter of the state of the test


def start_driver(browser=None):
    """ Initializes Web Driver

    :param browser: browser is used to determine which webdriver to initialize
    :return: driver object
    """
    print("=" * 50)
    print("Executing test: " + os.environ.get('PYTEST_CURRENT_TEST'))
    print("=" * 50)
    web_page = os.path.join(current_dir, 'Paylocity QA Interview Challenge', 'home.html')
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=os.path.join(current_dir, 'webdriver', 'chromedriver.exe'))
    elif browser == "firefox":
        web_page = "file:///" + web_page  # required only for Firefox webdriver
        driver = webdriver.Firefox(executable_path=os.path.join(current_dir, 'webdriver', 'geckodriver.exe'))

    driver.get(web_page)  # Opens a web page
    driver.maximize_window()  # Maximizes current browser window
    return driver  # Returns driver object
