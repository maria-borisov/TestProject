"""
__author__= Maria Borisov

"""

# Imports
import pytest
from Utilities import utils

class Test_Webpage():
    """ Test Class: Includes all Dashboard test cases """


    @pytest.mark.dashboard
    def test_add_new_employee(self, browser_login_setup):
        """
        Adds a new employee with a given first name, last name and dependents.
        :param browser_login_setup: Value returned by browser_login_setup fixture
        :expect:  Employee is successfully created
        """
        utils.driver = browser_login_setup   # Value returned by browser_login_setup fixture
        # Create a new Employee
        employee = utils.employee_class(first_name="Steph", last_name="Curry", dependents=0)
        employee.add_new_employee()
        # Verify Employee data
        employee.verify_employee_data()


    @pytest.mark.dashboard
    def test_add_new_employee_with_a(self, browser_login_setup):
        """
        Adds a new employee with a given first name, last name and dependents.
        Where first name and last name start with "A".
        :param browser_login_setup: Value returned by browser_login_setup fixture
        :expect: Employee is successfully created and all calculation are correct
        """
        utils.driver = browser_login_setup
        # Create a new Employee
        employee = utils.employee_class(first_name="Andre", last_name="Agassi", dependents=0)
        employee.add_new_employee()
        # Verify Employee data
        employee.verify_employee_data()

    @pytest.mark.dashboard
    def test_edit_employee(self, browser_login_setup):
        """
        Edit existing employee with a given new first name, last name and dependents.
        :param browser_login_setup:Value returned by browser_login_setup fixture
        :expect: Employee is successfully edited and all calculations are correct
        """
        utils.driver = browser_login_setup
        # Create a new Employee
        employee = utils.employee_class(first_name="Michael", last_name="Jordan", dependents=5)
        employee.add_new_employee()
        # Edit Employee's data
        employee.edit_employee(new_firstname="Luka", new_lastname="Doncic", new_dependents=3)


    @pytest.mark.dashboard
    def test_delete_employee(self, browser_login_setup):
        """
        Delete existing employee.
        :param browser_login_setup: Value returned by browser_login_setup fixture
        :expect: Employee is successfully removed from the table.
        """
        utils.driver = browser_login_setup
        # Create a new Employee
        employee = utils.employee_class(first_name="Adam", last_name="Sandler", dependents=1)
        employee.add_new_employee()
        # Delete Employee
        employee.delete_employee()

