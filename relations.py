def check_reflexive(matrix):
    reflexive = True

    for row in range(len(matrix)):
        # row_pos = matrix.index(row)
        for col in range(len(matrix)):
            # col_pos = row.index(col)
            if row == col and not matrix[row][col] == 1:
                reflexive = False


    return reflexive

def make_reflexive(matrix):
    missing_values = []
    if not check_reflexive(matrix):
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                if row == col and not matrix[row][col] == 1:
                    missing_values.append([row, col])

    matrix_copy = matrix
    for missing in missing_values:
        matrix_copy[missing[0]][missing[1]] = 1

    return matrix_copy

def check_irreflexive(matrix):
    irreflexive = True

    for row in range(len(matrix)):
        # row_pos = matrix.index(row)
        for col in range(len(matrix)):
            # col_pos = row.index(col)
            if row == col and not matrix[row][col] == 0:
                irreflexive = False

    return irreflexive

def make_irreflexive(matrix):
    missing_values = []
    if not check_reflexive(matrix):
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                if row == col and not matrix[row][col] == 0:
                    missing_values.append([row, col])

    matrix_copy = matrix
    for missing in missing_values:
        matrix_copy[missing[0]][missing[1]] = 0

    return matrix_copy

def check_symmetric(matrix):
    symmetric = True
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 1 and matrix[col][row] == 0:
                symmetric = False

    return symmetric

def make_symmetric(matrix):
    missing_values = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 1 and matrix[col][row] == 0:
                missing_values.append([col, row])

    matrix_copy = matrix
    for missing in missing_values:
        matrix_copy[missing[0]][missing[1]] = 1
    return matrix_copy

def check_antisymmetric(matrix):
    pass

def make_antisymmetric(matrix):
    pass

def check_asymmetric(matrix):
    return check_antisymmetric(matrix) and check_irreflexive(matrix)

def make_asymmetric(matrix):
    pass