class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

    def __add__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]
            return result
        else:
            raise ValueError("Matrix dimensions must match for addition")

    def __sub__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] - other.data[i][j]
            return result
        else:
            raise ValueError("Matrix dimensions must match for subtraction")

    def __mul__(self, other):
        if self.cols == other.rows:
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    total = 0
                    for k in range(self.cols):
                        total += self.data[i][k] * other.data[k][j]
                    result.data[i][j] = total
            return result
        else:
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix for multiplication")


# Example usage:
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Addition
result_add = matrix1 + matrix2
print("Addition:")
print(result_add)

matrix3 = Matrix(2, 2)
matrix3.data = [[1, 2], [3, 4]]

matrix4 = Matrix(2, 2)
matrix4.data = [[5, 6], [7, 8]]

# Subtraction
result_sub = matrix3 - matrix4
print("Subtraction:")
print(result_sub)

matrix5 = Matrix(3, 2)
matrix5.data = [[1, 2], [3, 4], [5, 6]]

matrix6 = Matrix(2, 4)
matrix6.data = [[7, 8, 9, 10], [11, 12, 13, 14]]

# Multiplication
result_mul = matrix5 * matrix6
print("Multiplication:")
print(result_mul)

