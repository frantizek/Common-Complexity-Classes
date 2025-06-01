#
# Write a function that takes a list of integers and returns the first element.
# If the list is empty, it should return None.
#
# Input: A list of integers.
# Output: The first integer in the list or None.
#

def return_last_element(list_of_integers: list) -> int | None:
    if not list_of_integers:
        return None
    else:
        return list_of_integers[-1]


def return_first_element(list_of_integers: list) -> int | None:
    if not list_of_integers:
        return None
    else:
        return list_of_integers[0]


def single_liner_return_last_element(list_of_integers: list) -> int | None:
    return list_of_integers[-1] if list_of_integers else None


def single_liner_return_first_element(list_of_integers: list) -> int | None:
    return list_of_integers[0] if list_of_integers else None
