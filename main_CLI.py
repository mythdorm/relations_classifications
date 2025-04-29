import sys

import relations

possible_operations = ["Reflexive", "Irreflexive", "Symmetric", "Antisymmetric", "Asymmetric", "Transitive", "Equivalence"]

def get_matrix_size():
    matrix_size = 0
    entering_size = True
    while entering_size:
        try:
            matrix_size = int(input("Enter the size of matrix you wish to create: "))
            entering_size = False
        except ValueError:
            print("Please enter a number in integer format.")
    return matrix_size

def get_matrix(matrix_size):
    matrix_correct = False
    matrix = []
    while not matrix_correct:

        for i in range(matrix_size):
            row_input = input(
                f"Enter row {i + 1} of the matrix as 1's and 0's seperated by spaces (if the length of the row isn't {matrix_size}, it will be filled with 0's): ")
            row = row_input.split(" ")
            for k in range(len(row)):
                if row[k] == "" or not (row[k] == "1" or row[k] == "0"):
                    row[k] = "0"
            if len(row) < matrix_size:
                for j in range(matrix_size - len(row)):
                    row.append("0")
            elif len(row) > matrix_size:
                for j in range(len(row) - matrix_size):
                    row.remove(row[-1])
            matrix.append(row)

        print("\nIs the following matrix correct?")

        for row in matrix:
            row_str = " ".join(row)
            print(row_str)

        input_result = input("(Y/N): ")
        if input_result.upper() == "Y" or input_result.upper() == "YES":
            matrix_correct = True
        elif input_result.upper() == "N" or input_result.upper() == "NO":
            matrix = []

    return matrix

def get_check_or_fix():
    answer = ""
    is_check_or_fix = True
    while is_check_or_fix:
        answer = input("(CHECK/FIX): ")
        if answer.upper() == "CHECK" or answer.upper() == "FIX":
            is_check_or_fix = False
        else:
            print("Please enter either 'CHECK' or 'FIX'")
    return answer

def get_operation(answer):
    for operation in possible_operations:
        print(f"{possible_operations.index(operation) + 1}. {operation}")
    getting_operation = True
    while getting_operation:
        answer = input(f"(1-{len(possible_operations)}): ")
        try:
            answer = int(answer)
            if answer < 1 or answer > len(possible_operations):
                print(f"Please enter a number between 1 and {len(possible_operations)}")
            else:
                getting_operation = False
        except ValueError:
            print("Please enter a number in integer format.", file=sys.stderr)
    return answer

def print_check_result(result, build):
    if result == True:
        print(f"The matrix is {build[6:]}")
    else:
        print(f"The matrix is not {build[6:]}")

def copy_new_matrix(matrix):
    copy_matrix = []
    for row in matrix:
        copy_row = []
        for elem in row:
            copy_row.append(elem)
        copy_matrix.append(copy_row)
    return copy_matrix

def print_matrix(matrix):
    for row in matrix:
        row_str = ''
        for col in row:
            row_str += f"{col} "
        print(row_str)

def print_changes(matrix, result):
    print("The matrix has been changed from:")
    print_matrix(matrix)
    print("To:")
    print_matrix(result)

def results(build, matrix):
    if build == "check reflexive":
        result = relations.check_reflexive(matrix)
        print_check_result(result, build)
    elif build == "check irreflexive":
        result = relations.check_irreflexive(matrix)
        print_check_result(result, build)
    elif build == "check symmetric":
        result = relations.check_symmetric(matrix)
        print_check_result(result, build)
    elif build == "check antisymmetric":
        result = relations.check_antisymmetric(matrix)
        print_check_result(result, build)
    elif build == "check asymmetric":
        result = relations.check_asymmetric(matrix)
        print_check_result(result, build)
    elif build == "check transitive":
        result = relations.check_transitive(matrix)
        print_check_result(result, build)
    elif build == "check equivalence":
        result = relations.check_equivalence(matrix)
        print_check_result(result, build)
    elif build == "fix reflexive":
        copy_matrix = copy_new_matrix(matrix)
        result = relations.make_reflexive(copy_matrix)
        print_changes(matrix, result)
    elif build == "fix irreflexive":
        copy_matrix = copy_new_matrix(matrix)
        result = relations.make_irreflexive(copy_matrix)
        print_changes(matrix, result)
    elif build == "fix symmetric":
        copy_matrix = copy_new_matrix(matrix)
        result = relations.make_symmetric(copy_matrix)
        print_changes(matrix, result)
    elif build == "fix antisymmetric":
        copy_matrix = copy_new_matrix(matrix)
        result = relations.make_antisymmetric(copy_matrix)
        print_changes(matrix, result)
    elif build == "fix asymmetric":
        copy_matrix = copy_new_matrix(matrix)
        result = relations.make_asymmetric(copy_matrix)
        print_changes(matrix, result)
    elif build == "fix transitive":
        copy_matrix = copy_new_matrix(matrix)
        result = relations.make_transitive(copy_matrix)
        print_changes(matrix, result)
    elif build == "fix equivalence":
        copy_matrix = copy_new_matrix(matrix)
        result = relations.make_equivalence(copy_matrix)
        print_changes(matrix, result)

def get_continue():
    continuing = True
    while continuing:
        input_result = input("(Y/N): ")
        if input_result.upper() == "Y" or input_result.upper() == "YES":
            main_loop()
        elif not input_result.upper() == "N" and not input_result.upper() == "NO":
            print("Please enter either 'Y' or 'N'.")
        continuing = False

def main_loop():
    matrix_size = get_matrix_size()

    matrix = get_matrix(matrix_size)

    print("Would you like to CHECK the matrix or FIX the matrix?")

    answer = get_check_or_fix()

    build = answer.lower()

    print(f"\nSelect the operation you want to {answer.lower()}.")

    answer = get_operation(answer)

    build += f" {possible_operations[answer - 1]}".lower()

    results(build, matrix)

    print("Do you want to do another matrix?")

    get_continue()

def main():
    print("Welcome to the Relations Classification App")

    main_loop()



if __name__ == '__main__':
    main()