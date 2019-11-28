"""
__author__= Maria Borisov

"""

# Imports
import pytest
from Utilities import utils

class Test_login_page():
    """ Test Class: Includes all Login test cases """
    @pytest.mark.login
    @pytest.mark.valid_login
    def test_login_valid_user(self, browser_setup):
        """ Test method to use the Login page with a valid user

        :param browser_setup: Yield value from browser_setup fixture
        :expect : Login to succeed
        """
        utils.driver = browser_setup
        utils.helper_functions().login(username="testUser", password="Test1234")

    @pytest.mark.login
    @pytest.mark.invalid_login
    def test_test_login_invalid_user(self, browser_setup):
        """ Test method to use the Login page with an invalid user

        :param browser_setup: Yield value from browser_setup fixture
        :expect : Login to fail
        """
        utils.driver = browser_setup
        utils.helper_functions().login(username="testUser1", password="Test1234")
        assert "Invalid login attempt. Please try again." in utils.driver.find_element_by_id("validation-errors").text

