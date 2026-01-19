def main():
    matrix_1 = get_matrix()
    matrix_2 = [[1, 2], [3, 4]]

    # the user submitted matrix will be added with a static 2x2 matrix to get matrix_3
    matrix_3 = add_matrix(matrix_1, matrix_2)
    print(matrix_3)


def get_matrix():
    column_count = input("Input Number of Columns in the matrix: ")
    row_count = input("Input Number of Rows in the matrix: ")

    new_matrix = []
    for i in range(int(column_count)):
        new_matrix.append([])
        for j in range(int(row_count)):
            new_value = input(f"Input a value for cell [{i}, {j}]: ")
            new_matrix[i].append(int(new_value))

    return new_matrix 


def add_matrix(matrix_1, matrix_2):
    # first checks if the matrices share the same dimensions
    if len(matrix_1) == len(matrix_2) and len(matrix_1[0]) == len(matrix_2[0]):

        matrix_3 = []
        for i in range(len(matrix_1)):
            matrix_3.append([])
            for j in range(len(matrix_1[0])):
                added_value = matrix_1[i][j] + matrix_2[i][j]
                matrix_3[i].append(int(added_value))
        
        return matrix_3
            
    else:
        return "These matrices are incompatible."


if __name__ == '__main__':
    main()