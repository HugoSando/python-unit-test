import pytest
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(number_one = 2, number_two = 4)
    assert result == 6

def test_substract():
    result = my_functions.substract(number_one = 2, number_two = 4)
    assert result == -2

def test_multiply():
    result = my_functions.multiply(number_one = 2, number_two = 4)
    assert result == 8

def test_divide():
    result = my_functions.divide(number_one = 2, number_two = 4)
    assert result == 1/2

def test_divide_Zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(number_one = 2, number_two = 0)

def test_oddEven():
    result = my_functions.OddEven(number=5)
    assert result == "Odd"