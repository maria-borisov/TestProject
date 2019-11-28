# TestProject

Requirements:
    - Python 3.0 or higher (https://www.python.org/downloads/)
    - Install pip (https://pip.pypa.io/en/stable/installing/)
    - Install Python packages:
        cmd> pip install pytest selenium pytest-html

Execute tests:
    cmd> cd <root directory>
    cmd> pytest -s -m <marker_name> --html=.\logs\report.html

Example:
    cmd> pytest -s -m dashboard --html=.\logs\report.html

-s : standard output
-m : only run tests matching a given mark expression

Available Project Markers:
    login
    dashboard
    valid_login
    invalid_login

Note: If -m is not supplied, pytest is going to execute all the tests in the current directory.
--html : creates html report at the given path, if not supplied report will not be created

Results:
HTML report is saved in a reports\report.html file. It is overwritten with every test execution.




