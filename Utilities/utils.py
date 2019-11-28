"""
__author__= Maria Borisov

"""

# Imports
import time

# Initialize web driver
driver = None

class employee_class:
    """ Class: Includes all employee methods """

    def __init__(self, first_name=None, last_name=None, dependents=None):
        """
        This method will be executed every time an object is called.
        It calculates benefit cost, salary and gross pay for each employee.
        benefit_cost = (1000 + (number of dependents * 500)) / 26
        cost of benefits = $1000/year for each employee
        Each dependent incurs a cost of $500 / year
        There are 26 paychecks in a year.
        # employee's cost + number of dependents
        :param first_name: string
        :param last_name:  string
        :param dependents: integer
        """
        self.first_name = first_name
        self.last_name = last_name
        self.dependents = dependents
        self.benefit_cost = round((1000 + self.dependents * 500) / 26, 2)
        if self.first_name.lower().startswith("a"):              # Check that Employee first name starts with "a" or "A"
            self.benefit_cost = round(self.benefit_cost - (self.benefit_cost * 0.1), 2)  # benefit cost with 10% discount and rounded
        self.salary = "52000.00"
        self.gross_pay = "2000.00"

    def get_employee_table(self):
        """
        Collects all data from the Employee table.
        Adds collected data to a list of Dictionaries.

        :return: list of Dictionaries
        """
        # Collects all employees data and saves it into a list of Dictionaries
        all_amployees_list = []
        table = driver.find_element_by_xpath("//table[@id='employee-table']")
        table_rows = len(table.find_elements_by_tag_name("tr"))
        for row in range(table_rows):
            if row != 0:
                employee_id = driver.find_element_by_xpath(
                    "//table[@id='employee-table']/tbody/tr[" + str(row) + "]/td[1]")
                employee_firstname = driver.find_element_by_xpath(
                    "//table[@id='employee-table']/tbody/tr[" + str(row) + "]/td[3]")
                employee_lastname = driver.find_element_by_xpath(
                    "//table[@id='employee-table']/tbody/tr[" + str(row) + "]/td[2]")
                employee_salary = driver.find_element_by_xpath(
                    "//table[@id='employee-table']/tbody/tr[" + str(row) + "]/td[4]")
                employee_dependents = driver.find_element_by_xpath(
                    "//table[@id='employee-table']/tbody/tr[" + str(row) + "]/td[5]")
                employee_gross_pay = driver.find_element_by_xpath(
                    "//table[@id='employee-table']/tbody/tr[" + str(row) + "]/td[6]")
                employee_benefit_cost = driver.find_element_by_xpath(
                    "//table[@id='employee-table']/tbody/tr[" + str(row) + "]/td[7]")
                employee_net_pay = driver.find_element_by_xpath(
                    "//table[@id='employee-table']/tbody/tr[" + str(row) + "]/td[8]")
                employee_dict = {'employee_id': employee_id.text,
                            'employee_firstname': employee_firstname.text,
                            'employee_lastname': employee_lastname.text,
                            'employee_salary': employee_salary.text,
                            'employee_dependents': employee_dependents.text,
                            'employee_gross_pay': employee_gross_pay.text,
                            'employee_benefit_cost': employee_benefit_cost.text,
                            'employee_net_pay': employee_net_pay.text,
                            'row': row}                              # Adds employee data to a Dictionary
                all_amployees_list.append(employee_dict)             # Appends Dictionary to a list
        return all_amployees_list

    def add_new_employee(self):
        """
        Adds a new employee with a given first name, last name and dependents.
        Enters data into the form.
        :expect: Employee is added and their corresponding information exists into the table
        """
        add_employee_button = driver.find_element_by_id("btnAddEmployee")
        add_employee_button.click()
        time.sleep(2)
        # Verify "Add Employee & His dependents" window is displayed
        assert driver.find_element_by_class_name("modal-title").is_displayed()
        assert "Add Employee & His dependents" in driver.find_element_by_class_name("modal-title").text
        # Enter employee data
        firstname_textbox = driver.find_element_by_xpath("//form[@id='employees-form']/div[1]/div[1]/input[1]")
        firstname_textbox.send_keys(self.first_name)
        lastname_textbox = driver.find_element_by_xpath("//form[@id='employees-form']/div[2]/div[1]/input[1]")
        lastname_textbox.send_keys(self.last_name)
        dependents_textbox = driver.find_element_by_xpath("//form[@id='employees-form']/div[3]/div[1]/input[1]")
        dependents_textbox.send_keys(self.dependents)
        submit_button = driver.find_element_by_xpath("//form[@id='employees-form']/div[4]/div[1]/button[1]")
        submit_button.click()
        time.sleep(5)
        assert self.employee_exist(), "Employee data was not saved correctly!"


    def edit_employee(self, new_firstname=None, new_lastname=None, new_dependents=None):
        """
        Finds existing employee and edits their data
        :param new_firstname: string
        :param new_lastname:  string
        :param new_dependents: integer
        """

        for employee in self.get_employee_table():
            if self.first_name == employee['employee_firstname'] \
                    and self.last_name == employee['employee_lastname']:
                edit_button = driver.find_element_by_xpath(
                    "//table[@id='employee-table']/tbody/tr[" + str(employee['row']) + "]/td[9]/span[@title='Edit']")
                edit_button.click()
                time.sleep(5)
                assert driver.find_element_by_class_name("modal-title").is_displayed(), "Edit employee page is not displayed"
                assert "Add Employee & His dependents" in driver.find_element_by_class_name("modal-title").text
                # Update Employee data
                firstname_textbox = driver.find_element_by_xpath("//form[@id='employees-form']/div[1]/div[1]/input[1]")
                if new_firstname is not None:
                    firstname_textbox.clear()
                    firstname_textbox.send_keys(new_firstname)
                lastname_textbox = driver.find_element_by_xpath("//form[@id='employees-form']/div[2]/div[1]/input[1]")
                if new_lastname is not None:
                    lastname_textbox.clear()
                    lastname_textbox.send_keys(new_lastname)
                dependents_textbox = driver.find_element_by_xpath("//form[@id='employees-form']/div[3]/div[1]/input[1]")
                if new_dependents is not None:
                    dependents_textbox.clear()
                    dependents_textbox.send_keys(new_dependents)
                submit_button = driver.find_element_by_xpath("//form[@id='employees-form']/div[4]/div[1]/button[1]")
                submit_button.click()
                time.sleep(2)

    def verify_employee_data(self):
        """
        Finds employee in the table.
        Verifies calculations in the table are correct.
        """
        assert "Benefits Dashboard" in driver.title

        for employee in self.get_employee_table():
            # Check If all the supplied data matches with the table
            if self.first_name == employee['employee_firstname'] and \
                    self.last_name == employee['employee_lastname'] and \
                    self.dependents == int(employee['employee_dependents']):
                print("Verifying data for: " + self.first_name + " " + self.last_name)
                assert employee['employee_salary'] == self.salary, "Incorrect salary: " + employee['employee_salary']
                assert employee['employee_gross_pay'] == self.gross_pay, "Incorrect gross pay: " + employee['employee_gross_pay']
                assert float(employee['employee_benefit_cost']) + float(employee['employee_net_pay']) == float(
                    employee['employee_gross_pay'])
                assert float(employee['employee_benefit_cost']) == self.benefit_cost, \
                    "Incorrect benefit cost: " + employee['employee_benefit_cost']
                print("Data is correct!")

    def delete_employee(self):
        """
        Finds employee in the table.
        Deletes employee from the table.
        Verifies employee doesn't exist in the table any more.
        """

        for employee in self.get_employee_table():
            if self.first_name == employee['employee_firstname'] \
                    and self.last_name == employee['employee_lastname']:
                # Delete Employee
                print("Delete: " + employee['employee_firstname'] + " " + employee['employee_lastname'])
                delete_button = driver.find_element_by_xpath("//table[@id='employee-table']/tbody/tr[" +
                                                             str(employee['row']) +
                                                             "]/td[9]/span[@title='Delete']")
                try:
                    delete_button.click()
                except:
                    print("Failed to delete: " + self.first_name + " " + self.last_name)

                time.sleep(10)
                print("Employee: " + self.first_name + " " + self.last_name + " has been deleted!")
            assert not self.employee_exist(), "Failed to delete employee!"

    def employee_exist(self):
        """
        Verifies that employee exists in the table
        :return: True - if employee exists; False - if employee doesn't exist
        """

        for employee in self.get_employee_table():
            if self.first_name == employee['employee_firstname'] \
                    and self.last_name == employee['employee_lastname']:
                return True
        return False

    def close_employees_window(self):
        """
        Closes Add New Employee window
        """
        # Close "Add new Employees" window
        submit_button = driver.find_element_by_xpath("//form[@id='employees-form']/div[4]/div[1]/button[2]")
        submit_button.click()

class helper_functions:
    """ Test helper methods """
    def login(self, username=None, password=None):
        """
        Logs in using given username and password
        :param username:
        :param password:
        """
        username_textbox = driver.find_element_by_name("form-username")
        username_textbox.send_keys(username)  # Enter username in the text field
        password_textbox = driver.find_element_by_name("form-password")
        password_textbox.send_keys(password)  # Enter Password in the text field
        login_button = driver.find_element_by_class_name("btn-primary")
        login_button.click()  # Click on the Login button

