import pytest
from employee import Employee

@pytest.fixture
def employee():
    """
    Return a sample employee instance for testing.
    """
    return Employee("Alice", "Smith", 50000)

def test_give_default_raise(employee):
    """
    Test if the employee's annual salary gets incremented
    by the default amount.
    """
    employee.give_raise()
    assert employee.annual_salary == 55000

def test_give_custom_raise(employee):
    """
    Test if the employee's annual salary is incremented with
    the given raise amount.
    """
    employee.give_raise(10000)
    assert employee.annual_salary == 60000