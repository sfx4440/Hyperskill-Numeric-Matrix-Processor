def add_matrices():
    x, y = [int(i) for i in input('Enter size of first matrix: ').split()]
    print("Enter first matrix:")
    matrix_a = [[float(i) for i in input().split()] for _ in range(x)]

    v, w = [int(i) for i in input('Enter size of second matrix: ').split()]
    print("Enter second matrix:")
    matrix_b = [[float(i) for i in input().split()] for _ in range(v)]

    if x != v or y != w:
        print('ERROR')
    else:
        total_matrix = [[matrix_a[i][j] + matrix_b[i][j] for j in range(y)] for i in range(x)]
        print("The result is:")
        [print(*arg) for arg in total_matrix]
    intro_prompt()


def matrix_scalar():
    x, y = [int(i) for i in input("Enter size of matrix: ").split()]
    print("Enter matrix:")
    matrix_a = [[float(i) for i in input().split()] for _ in range(x)]

    multiplier = float(input("Enter constant: "))

    multi_matrix = [[matrix_a[i][j] * multiplier for j in range(y)] for i in range(x)]
    print("The result is:")
    [print(*arg) for arg in multi_matrix]
    intro_prompt()


def matrix_multiplier():
    x, y = [int(i) for i in input('Enter size of first matrix: ').split()]
    print("Enter first matrix:")
    matrix_a = [[float(i) for i in input().split()] for _ in range(x)]

    v, w = [int(i) for i in input('Enter size of second matrix: ').split()]
    print("Enter second matrix:")
    matrix_b = [[float(i) for i in input().split()] for _ in range(v)]

    if y != v:
        print('ERROR')
    else:
        new_matrix = [[float(0) for _ in range(len(matrix_b))] for _ in range(len(matrix_b[0]))]

        times_matrix = [[float(0) for _ in range(len(matrix_a))] for _ in range(len(matrix_b[0]))]

        transposed_matrix = [[float(0) for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]

        for i in range(len(matrix_b[0])):
            for j in range(len(matrix_b)):
                new_matrix[i][j] = matrix_b[j][i]

        for n in range(len(new_matrix)):
            for j in range(len(matrix_a)):
                multi_value = 0
                for i in range(len(new_matrix[n])):
                    
                    multi_value += (new_matrix[n][i] * matrix_a[j][i])
                times_matrix[n][j] = multi_value

        for i in range(len(times_matrix[0])):
            for j in range(len(times_matrix)):
                transposed_matrix[i][j] = times_matrix[j][i]

        print("The result is:")
        [print(*arg) for arg in transposed_matrix]
    intro_prompt()


def regular_transpose():
    x, y = [int(i) for i in input('Enter size of matrix: ').split()]
    print("Enter matrix:")
    matrix_a = [[float(i) for i in input().split()] for _ in range(x)]
    new_matrix = [[float(0) for _ in matrix_a[0]] for _ in matrix_a]

    for i in range(len(matrix_a[0])):
        for j in range(len(matrix_a)):
            new_matrix[i][j] = matrix_a[j][i]

    print("The result is:")
    [print(*arg) for arg in new_matrix]


def reverse_transpose():
    x, y = [int(i) for i in input('Enter size of matrix: ').split()]
    print("Enter matrix:")
    matrix_a = [[float(i) for i in input().split()] for _ in range(x)]
    new_matrix = [[float(0) for _ in matrix_a[0]] for _ in matrix_a]

    for i in range(len(matrix_a[0])):
        for j in range(len(matrix_a)):
            new_matrix[len(matrix_a[0])-1-i][len(matrix_a[0])-1-j] = matrix_a[j][i]

    print("The result is:")
    [print(*arg) for arg in new_matrix]


def vertical_transpose():
    x, y = [int(i) for i in input('Enter size of matrix: ').split()]
    print("Enter matrix:")
    matrix_a = [[float(i) for i in input().split()] for _ in range(x)]
    new_matrix = [[float(0) for _ in matrix_a[0]] for _ in matrix_a]

    for i in range(len(matrix_a[0])):
        for j in range(len(matrix_a)):
            new_matrix[i][len(matrix_a[0])-1-j] = matrix_a[i][j]

    print("The result is:")
    [print(*arg) for arg in new_matrix]


def horizontal_transpose():
    x, y = [int(i) for i in input('Enter size of matrix: ').split()]
    print("Enter matrix:")
    matrix_a = [[float(i) for i in input().split()] for _ in range(x)]
    new_matrix = [[float(0) for _ in matrix_a[0]] for _ in matrix_a]

    for i in range(len(matrix_a[0])):
        for j in range(len(matrix_a)):
            new_matrix[len(matrix_a)-1-i][j] = matrix_a[i][j]

    print("The result is:")
    [print(*arg) for arg in new_matrix]


def transpose_menu():
    choice = int(input("""\
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
"""))
    if choice == 1:
        regular_transpose()
    elif choice == 2:
        reverse_transpose()
    elif choice == 3:
        vertical_transpose()
    elif choice == 4:
        horizontal_transpose()
    else:
        print('Invalid selection. Please try again.')
        transpose_menu()


def minor(matrix, i, j):
    if len(matrix[0]) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    elif len(matrix[0]) > 2:
        ml = [[float(matrix[v][w]) for w in range(len(matrix[v])) if w != j] for v in range(len(matrix)) if v != i]
        return ml


def determinant(matrix):
    if type(matrix) is not list:
        return matrix
    elif len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return (-1)**2 * determinant(minor(matrix, 0, 0))
    elif len(matrix) > 2:
        determinant_recursion = 0.0
        for i in range(len(matrix[0])):
            determinant_recursion += matrix[0][i] * ((-1) ** (i + 2)) * determinant(minor(matrix, 0, i))
        return determinant_recursion


def determinant_choice():
    x, y = [int(i) for i in input('Enter size of matrix: ').split()]
    print("Enter matrix:")
    matrix_a = [[float(i) for i in input().split()] for _ in range(x)]
    print(f"The result is:\n", determinant(matrix_a))


def cofactor_matrix(matrix):
    cofactor_matrix = [[float(0) for _ in matrix[0]] for _ in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            cofactor_matrix[i][j] = ((-1) ** (i + j + 2)) * determinant(minor(matrix, i, j))
    return cofactor_matrix


def inverse(matrix):
    if determinant(matrix) == 0:
        print("This matrix doesn't have an inverse")
        intro_prompt()
    else:
        adjoint = cofactor_matrix(matrix)
        multiplier = 1 / determinant(matrix)
        transpose_adjoint = [[float(0) for _ in matrix[0]] for _ in matrix]
        for i in range(len(adjoint[0])):
            for j in range(len(adjoint)):
                transpose_adjoint[i][j] = adjoint[j][i]
        multi_matrix = [[transpose_adjoint[i][j] * multiplier
                         for j in range(len(transpose_adjoint[i]))]
                        for i in range(len(transpose_adjoint))]
        return multi_matrix


def inverse_choice():
    x, y = [int(i) for i in input('Enter size of matrix: ').split()]
    print("Enter matrix:")
    matrix = [[float(i) for i in input().split()] for _ in range(x)]
    print(f"The result is:\n")
    [print(*arg) for arg in inverse(matrix)]


def intro_prompt():
    choice = int(input("""\
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse Matrix
0. Exit
"""))
    if choice == 1:
        add_matrices()
    elif choice == 2:
        matrix_scalar()
    elif choice == 3:
        matrix_multiplier()
    elif choice == 4:
        transpose_menu()
    elif choice == 5:
        determinant_choice()
    elif choice == 6:
        inverse_choice()
    elif choice == 0:
        exit()
    else:
        print('Invalid selection. Please try again.')
        intro_prompt()


intro_prompt()
