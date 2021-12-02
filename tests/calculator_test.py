"""Testing the Calculator"""
import calc as calc
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations


@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()


@pytest.fixture
def test_tuple():
    my_tuple = (1.0, 2.0, 5.0)
    return my_tuple


# You have to add the fixture function as a parameter to the test that you want to use it with
def test_calculator_add_static(clear_history_fixture, test_tuple):
    """testing that our calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    # using Tuple instead of args because we can pack as much data as we need into the tuple
    Calculator.add_numbers(test_tuple)
    assert Calculator.get_result_value() == 8.0


def test_calculator_subtract_static(clear_history_fixture, test_tuple):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    # using Tuple instead of args because we can pack as much data as we need into the tuple
    Calculator.subtract_numbers(test_tuple)
    assert Calculator.get_result_value() == -8.0


def test_calculator_multiply_static(clear_history_fixture, test_tuple):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    # using Tuple instead of args because we can pack as much data as we need into the tuple
    Calculator.multiply_numbers(test_tuple)
    assert Calculator.get_result_value() == 10.0


def test_calculator_divide(clear_history_fixture, test_tuple):
    Calculator.divide_numbers(test_tuple)
    assert Calculator.get_result_value() != 0
    print("An error occurred")
