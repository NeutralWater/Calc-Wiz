from formulas import linear_algebra
from topic_lib import linear_algebra_lib
import formula_display.display_linear_algebra as fd
import formula_display.core as core

def show_formula(formula):
    core.display_formula(formula)


def get_vector(name):
    data = input(f"Enter {name} vector values (comma-separated): ")
    return [float(x.strip()) for x in data.split(",")]

def get_vectors():
    count = int(input("Number of vectors: "))
    vectors = []

    for i in range(count):
        vectors.append(get_vector(f"vector {i + 1}"))

    return vectors

def get_matrix(name):
    rows = int(input(f"Rows in {name}: "))
    cols = int(input(f"Columns in {name}: "))

    matrix = []

    for i in range(rows):
        while True:
            row = [float(x.strip()) for x in input(
                f"{name} row {i + 1} values (comma-separated): "
            ).split(",")]

            if len(row) == cols:
                matrix.append(row)
                break

            print(f"Please enter exactly {cols} values.")

    return matrix


def run_linear_algebra():
    linear_algebra_lib()
    choice = input("Select a formula: ")
    print("")

    if choice == "1":
        v1 = get_vector("first")
        v2 = get_vector("second")
        print("")

        result = linear_algebra.dot_product(v1, v2)

        if result is None:
            print("Vectors must have the same number of components.")
        else:
            print(f"Dot Product = {result}")

        show_formula(fd.dot_product())
        print("")

    elif choice == "2":
        v = get_vector("vector")
        print("")
        print(f"Magnitude = {linear_algebra.magnitude(v)}")
        show_formula(fd.magnitude())
        print("")

    elif choice == "3":
        v = get_vector("vector")
        print("")

        result = linear_algebra.unit_vector(v)

        if result is None:
            print("The zero vector has no unit vector.")
        else:
            print(f"Unit Vector = {result}")

        show_formula(fd.unit_vector())
        print("")

    elif choice == "4":
        v1 = get_vector("first")
        v2 = get_vector("second")
        print("")

        result = linear_algebra.vector_addition(v1, v2)

        if result is None:
            print("Vectors must have the same number of components.")
        else:
            print(f"Vector Sum = {result}")

        show_formula(fd.vector_addition())
        print("")

    elif choice == "5":
        v1 = get_vector("first")
        v2 = get_vector("second")
        print("")

        result = linear_algebra.vector_subtraction(v1, v2)

        if result is None:
            print("Vectors must have the same number of components.")
        else:
            print(f"Vector Difference = {result}")

        show_formula(fd.vector_subtraction())
        print("")

    elif choice == "6":
        c = float(input("Scalar: "))
        v = get_vector("vector")
        print("")
        print(f"Scalar Product = {linear_algebra.scalar_multiplication(c, v)}")
        show_formula(fd.scalar_multiplication())
        print("")

    elif choice == "7":
        v1 = get_vector("first")
        v2 = get_vector("second")
        print("")

        result = linear_algebra.cross_product(v1, v2)

        if result is None:
            print("Cross product only works for 3D vectors.")
        else:
            print(f"Cross Product = {result}")

        show_formula(fd.cross_product())
        print("")

    elif choice == "8":
        A = get_matrix("A")
        B = get_matrix("B")
        print("")

        result = linear_algebra.matrix_addition(A, B)

        if result is None:
            print("Matrices must have the same dimensions.")
        else:
            print(f"Matrix Sum = {result}")

        show_formula(fd.matrix_addition())
        print("")

    elif choice == "9":
        A = get_matrix("A")
        B = get_matrix("B")
        print("")

        result = linear_algebra.matrix_subtraction(A, B)

        if result is None:
            print("Matrices must have the same dimensions.")
        else:
            print(f"Matrix Difference = {result}")

        show_formula(fd.matrix_subtraction())
        print("")

    elif choice == "10":
        A = get_matrix("A")
        B = get_matrix("B")
        print("")

        result = linear_algebra.matrix_multiplication(A, B)

        if result is None:
            print("Columns of A must equal rows of B.")
        else:
            print(f"Matrix Product = {result}")

        show_formula(fd.matrix_multiplication())
        print("")

    elif choice == "11":
        A = get_matrix("A")
        print("")
        print(f"Transpose = {linear_algebra.transpose(A)}")
        show_formula(fd.transpose())
        print("")

    elif choice == "12":
        A = get_matrix("A")
        print("")

        result = linear_algebra.determinant_2x2(A)

        if result is None:
            print("Determinant option only supports 2x2 matrices right now.")
        else:
            print(f"Determinant = {result}")

        show_formula(fd.determinant_2x2())
        print("")

    elif choice == "13":
        A = get_matrix("A")
        print("")

        result = linear_algebra.trace(A)

        if result is None:
            print("Trace only works for square matrices.")
        else:
            print(f"Trace = {result}")

        show_formula(fd.trace())
        print("")
    
    elif choice == "14":
        A = get_matrix("A")
        print("")
        result = linear_algebra.matrix_inverse(A)

        if result is None:
            print("Matrix must be square and invertible.")
        else:
            print(f"Inverse = {result}")

        show_formula(fd.matrix_inverse())
        print("")

    elif choice == "15":
        A = get_matrix("A")
        print("")
        print(f"Rank = {linear_algebra.matrix_rank(A)}")
        show_formula(fd.matrix_rank())
        print("")

    elif choice == "16":
        A = get_matrix("A")
        print("")
        print(f"RREF = {linear_algebra.rref(A)}")
        show_formula(fd.rref())
        print("")

    elif choice == "17":
        A = get_matrix("A")
        print("")
        result = linear_algebra.determinant(A)

        if result is None:
            print("Determinant only works for square matrices.")
        else:
            print(f"Determinant = {result}")

        show_formula(fd.determinant())
        print("")

    elif choice == "18":
        v1 = get_vector("first")
        v2 = get_vector("second")
        print("")
        result = linear_algebra.angle_between_vectors(v1, v2)

        if result is None:
            print("Vectors must have same dimensions and cannot be zero vectors.")
        else:
            print(f"Angle = {result} degrees")

        show_formula(fd.angle_between_vectors())
        print("")

    elif choice == "19":
        v1 = get_vector("vector")
        v2 = get_vector("projection target")
        print("")
        result = linear_algebra.vector_projection(v1, v2)

        if result is None:
            print("Projection target cannot be the zero vector.")
        else:
            print(f"Projection = {result}")

        show_formula(fd.vector_projection())
        print("")

    elif choice == "20":
        v1 = get_vector("first")
        v2 = get_vector("second")
        print("")
        result = linear_algebra.distance_between_vectors(v1, v2)

        if result is None:
            print("Vectors must have the same number of components.")
        else:
            print(f"Distance = {result}")

        show_formula(fd.distance_between_vectors())
        print("")
    
    elif choice == "21":
        A = get_matrix("A")
        print(f"Eigenvalues = {linear_algebra.eigenvalues(A)}")
        show_formula(fd.eigenvalues())

    elif choice == "22":
        A = get_matrix("A")
        print(f"Eigenvectors = {linear_algebra.eigenvectors(A)}")
        show_formula(fd.eigenvectors())

    elif choice == "23":
        A = get_matrix("A")
        print(f"Characteristic Polynomial = {linear_algebra.characteristic_polynomial(A)}")
        show_formula(fd.characteristic_polynomial())

    elif choice == "24":
        A = get_matrix("A")
        print(f"Null Space = {linear_algebra.null_space(A)}")
        show_formula(fd.null_space())

    elif choice == "25":
        A = get_matrix("A")
        print(f"Column Space = {linear_algebra.column_space(A)}")
        show_formula(fd.column_space())

    elif choice == "26":
        A = get_matrix("A")
        print(f"Row Space = {linear_algebra.row_space(A)}")
        show_formula(fd.row_space())

    elif choice == "27":
        vectors = get_vectors()
        print(f"Gram-Schmidt Result = {linear_algebra.gram_schmidt(vectors)}")
        show_formula(fd.gram_schmidt())

    elif choice == "28":
        vectors = get_vectors()
        print(f"Linearly Independent = {linear_algebra.linear_independence(vectors)}")
        show_formula(fd.linear_independence())

    elif choice == "29":
        A = get_matrix("A")
        print(f"LU Decomposition = {linear_algebra.lu_decomposition(A)}")
        show_formula(fd.lu_decomposition())

    elif choice == "30":
        A = get_matrix("A")
        print(f"QR Decomposition = {linear_algebra.qr_decomposition(A)}")
        show_formula(fd.qr_decomposition())

    elif choice == "31":
        A = get_matrix("A")
        print(f"Matrix Norm = {linear_algebra.matrix_norm(A)}")
        show_formula(fd.matrix_norm())

    elif choice == "32":
        A = get_matrix("A")
        print(f"Orthogonal = {linear_algebra.is_orthogonal(A)}")
        show_formula(fd.orthogonal_matrix_check())

    elif choice == "33":
        A = get_matrix("A")
        print(f"Symmetric = {linear_algebra.is_symmetric(A)}")
        show_formula(fd.symmetric_matrix_check())

    elif choice == "34":
        A = get_matrix("A")
        print(f"Skew-Symmetric = {linear_algebra.is_skew_symmetric(A)}")
        show_formula(fd.skew_symmetric_matrix_check())

    elif choice == "35":
        A = get_matrix("A")
        print(f"Diagonalizable = {linear_algebra.is_diagonalizable(A)}")
        show_formula(fd.diagonalization_check())

    elif choice == "0":
        exit()