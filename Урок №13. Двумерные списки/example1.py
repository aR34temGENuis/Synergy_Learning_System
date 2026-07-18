import random


def create_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        row = []

        for j in range(cols):
            row.append(random.randint(-100, 100))

        matrix.append(row)

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


def add_matrices(matrix_1, matrix_2):
    result = []

    for i in range(len(matrix_1)):
        row = []

        for j in range(len(matrix_1[i])):
            row.append(matrix_1[i][j] + matrix_2[i][j])

        result.append(row)

    return result


rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix_1 = create_matrix(rows, cols)
matrix_2 = create_matrix(rows, cols)

print("Первая матрица:")
print_matrix(matrix_1)

print("Вторая матрица:")
print_matrix(matrix_2)

matrix_3 = add_matrices(matrix_1, matrix_2)

print("Сумма матриц:")
print_matrix(matrix_3)