import math


def dot_product(v1, v2):
    if len(v1) != len(v2):
        return None

    return sum(v1[i] * v2[i] for i in range(len(v1)))


def magnitude(v):
    return math.sqrt(sum(x ** 2 for x in v))


def unit_vector(v):
    mag = magnitude(v)

    if mag == 0:
        return None

    return [x / mag for x in v]


def vector_addition(v1, v2):
    if len(v1) != len(v2):
        return None

    return [v1[i] + v2[i] for i in range(len(v1))]


def vector_subtraction(v1, v2):
    if len(v1) != len(v2):
        return None

    return [v1[i] - v2[i] for i in range(len(v1))]


def scalar_multiplication(c, v):
    return [c * x for x in v]


def cross_product(v1, v2):
    if len(v1) != 3 or len(v2) != 3:
        return None

    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]


def same_dimensions(A, B):
    if len(A) != len(B):
        return False

    for i in range(len(A)):
        if len(A[i]) != len(B[i]):
            return False

    return True


def matrix_addition(A, B):
    if not same_dimensions(A, B):
        return None

    return [
        [A[i][j] + B[i][j] for j in range(len(A[i]))]
        for i in range(len(A))
    ]


def matrix_subtraction(A, B):
    if not same_dimensions(A, B):
        return None

    return [
        [A[i][j] - B[i][j] for j in range(len(A[i]))]
        for i in range(len(A))
    ]


def matrix_multiplication(A, B):
    if len(A[0]) != len(B):
        return None

    return [
        [
            sum(A[i][k] * B[k][j] for k in range(len(B)))
            for j in range(len(B[0]))
        ]
        for i in range(len(A))
    ]


def transpose(A):
    return [
        [A[i][j] for i in range(len(A))]
        for j in range(len(A[0]))
    ]


def determinant_2x2(A):
    if len(A) != 2 or len(A[0]) != 2 or len(A[1]) != 2:
        return None

    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def trace(A):
    if len(A) == 0:
        return None

    for row in A:
        if len(row) != len(A):
            return None

    return sum(A[i][i] for i in range(len(A)))