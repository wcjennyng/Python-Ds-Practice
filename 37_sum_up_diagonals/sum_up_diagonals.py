def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    sum = 0

    for i in range(len(matrix)):
        # sum over the main diagonal from [0, 0] to [size, size]
        sum += matrix[i][i]

        # sum over the other diagonal going from [0, size] to [size, 0]
        sum += matrix[i][-i-1]
    return sum