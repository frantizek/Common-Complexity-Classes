from constant_complexity_001 import (return_last_element, return_first_element,
                                     single_liner_return_first_element, single_liner_return_last_element)

def test_return_first_element_with_values():
    assert return_first_element([5, 6, 7]) == 5

def test_return_first_element_empty():
    assert return_first_element([]) is None

def test_return_last_element_with_values():
    assert return_last_element([1, 2, 3]) == 3

def test_return_last_element_empty():
    assert return_last_element([]) is None

def test_single_liner_return_first_element_with_values():
    assert single_liner_return_first_element([5, 6, 7]) == 5

def test_single_liner_return_first_element_empty():
    assert single_liner_return_first_element([]) is None

def test_single_liner_return_last_element_with_values():
    assert single_liner_return_last_element([1, 2, 3]) == 3

def test_single_liner_return_last_element_empty():
    assert single_liner_return_first_element([]) is None