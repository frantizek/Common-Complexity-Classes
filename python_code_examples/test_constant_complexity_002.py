from constant_complexity_002 import access_an_element

# --- Basic Valid Access ---
def test_access_first_element():
    assert access_an_element([[10, 20], [30, 40]], 0, 0) == 10

def test_access_last_element():
    assert access_an_element([[10, 20], [30, 40]], 1, 1) == 40

def test_access_middle_element():
    assert access_an_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1) == 5


# --- Empty Matrix ---
def test_empty_matrix():
    assert access_an_element([], 0, 0) is None

def test_matrix_with_empty_rows():
    assert access_an_element([[], [], []], 0, 0) is None


# --- Invalid Rows (Not Lists) ---
def test_row_is_not_a_list():
    assert access_an_element([123, [4, 5]], 0, 0) is None

def test_mixed_invalid_and_valid_rows():
    assert access_an_element(["not a list", [1, 2], 3], 1, 0) == 1


# --- Jagged Matrix (Inconsistent Row Lengths) ---
def test_access_out_of_bounds_in_jagged_matrix():
    assert access_an_element([[1, 2], [3]], 1, 1) is None

def test_access_valid_index_in_jagged_matrix():
    assert access_an_element([[1, 2], [3]], 0, 1) == 2


# --- Out-of-Bounds Indices ---
def test_row_index_too_large():
    assert access_an_element([[1, 2], [3, 4]], 2, 0) is None

def test_column_index_too_large():
    assert access_an_element([[1, 2], [3, 4]], 0, 2) is None

def test_negative_row_index():
    assert access_an_element([[1, 2], [3, 4]], -1, 0) is None

def test_negative_column_index():
    assert access_an_element([[1, 2], [3, 4]], 0, -1) is None


# --- Non-Matrix Inputs ---
def test_input_is_not_a_matrix():
    assert access_an_element("not a matrix", 0, 0) is None

def test_input_is_none():
    assert access_an_element(None, 0, 0) is None

def test_input_is_single_list():
    assert access_an_element([1, 2, 3], 0, 0) is None


# --- Single Row or Column ---
# def test_single_row_access():
#    assert access_an_element([[1]][[2]][[3]], 0, 1) == 2

def test_single_column_access():
    assert access_an_element([[1], [2], [3]], 2, 0) == 3

def test_single_cell_matrix():
    assert access_an_element([[42]], 0, 0) == 42


# --- Type Edge Cases ---
def test_matrix_with_none_inside():
    assert access_an_element([[None, 2], [3, 4]], 0, 0) is None

# def test_matrix_with_non_int_indices():
#    assert access_an_element([[1, 2], [3, 4]], "0", 0) is None

def test_matrix_with_boolean_input():
    assert access_an_element(True, 0, 0) is None