# Problem: Given a 2D matrix,
# write a function to access an element at a given row and column index.
# Input: A 2D matrix and the row and column indices.
# Output: The element at the specified position.


def access_an_element(matrix: list[list] , row_index: int, column_index:int):
    if not matrix:
        return None

    if isinstance(matrix, list) and all(isinstance(row, list) for row in matrix) and all(len(row) > 0 for row in matrix):
        max_rows = len(matrix)
        max_columns = 0
        for row in matrix:
            if len(row)>max_columns:
                max_columns = len(row)
            #print(row)
        #print(f"This matrix has {max_rows} rows and {max_columns} columns.")

        if isinstance(row_index, int) and isinstance(column_index, int):
            if 0 < row_index < max_rows and 0 < column_index < max_columns:
                return matrix[row_index][column_index]
    return None
