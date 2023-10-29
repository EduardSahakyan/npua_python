import random

def generate_random_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(cols)]
        matrix.append(row)
    return matrix

def get_column_sum(matrix, column_index):
    if not matrix:
        return 0
    if column_index < 0 or column_index >= len(matrix[0]):
        return 0
    return sum(row[column_index] for row in matrix)

def get_row_average(matrix, row_index):
    if not matrix:
        return 0
    if row_index < 0 or row_index >= len(matrix):
        return 0
    row = matrix[row_index]
    if not row:
        return 0
    return sum(row) / len(row)

matrix = generate_random_matrix(5, 6)
print("Random matrix:")
for row in matrix:
    print(row)

column_index = 3
column_sum = get_column_sum(matrix, column_index)
print(f"Sum of column {column_index}: {column_sum}")

row_index = 1
row_average = get_row_average(matrix, row_index)
print(f"Average of row {row_index}: {row_average}")
