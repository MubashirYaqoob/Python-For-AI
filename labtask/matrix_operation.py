
# --- Print Matrix ---
def print_matrix(matrix):
    print()
    for row in matrix:
        for val in row:
            print(f"{val:6}", end="")
        print()
    print()

# --- Input Matrix ---
def input_matrix(name):
    print(f"\n{name} enter size:")
    rows = int(input("  Rows: "))
    cols = int(input("  Cols: "))

    matrix = []
    print(f"\n{name} enter elements:")
    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input(f"  [{i}][{j}]: "))
            row.append(val)        
        matrix.append(row)         
    return matrix

# --- Validation ---
def validate(A, B, op):
    rowsA, colsA = len(A), len(A[0])
    rowsB, colsB = len(B), len(B[0])

    if op in ["add", "sub"]:
        if rowsA != rowsB or colsA != colsB:
            print(f"  Error: Same should be same A={rowsA}x{colsA}, B={rowsB}x{colsB}")
            return False
    elif op == "multiply":
        if colsA != rowsB:
            print(f"  Error: A  cols ({colsA}) == B  rows ({rowsB}) must be equal!")
            return False
    return True

# --- Addition ---
def addition(A, B):
    rows = len(A)
    cols = len(A[0])              
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] + B[i][j]
    return result

# --- Subtraction ---
def subtraction(A, B):
    rows = len(A)
    cols = len(A[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] - B[i][j]
    return result

# --- Multiplication ---
def multiply(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    colsB = len(B[0])
    C = [[0] * colsB for _ in range(rowsA)]
    for i in range(rowsA):
        for j in range(colsB):
            for k in range(colsA):
                C[i][j] += A[i][k] * B[k][j]
    return C

# --- Transpose ---
def transpose(A):                  
    rows = len(A)
    cols = len(A[0])
    C = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            C[j][i] = A[i][j]
    return C


# --- Determinant 2x2 ---
def det_2x2(A):
    if len(A) != 2 or len(A[0]) != 2:
        print("  Error: Only 2*2 matrix handle!")
        return None
    return A[0][0]*A[1][1] - A[0][1]*A[1][0]

# --- Determinant 3x3 ---
def det_3x3(A):
    if len(A) != 3 or len(A[0]) != 3:
        print("  Error: only 3x3  matrix determinant!")
        return None
    a,b,c = A[0][0], A[0][1], A[0][2]
    d,e,f = A[1][0], A[1][1], A[1][2]
    g,h,i = A[2][0], A[2][1], A[2][2]
    return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)


def menu():
    A = None
    B = None

    while True:
        print("\n=============================")
        print("     MATRIX CALCULATOR")
        print("=============================")
        print("  1. Input Matrix A")
        print("  2. Input Matrix B")
        print("  3. Addition       (A + B)")
        print("  4. Subtraction    (A - B)")
        print("  5. Multiplication (A x B)")
        print("  6. Transpose      (A)")
        print("  7. Scalar Multiply")
        print("  8. Determinant    (A)")
        print("  0. Exit")
        print("=============================")

        choice = input("  Choice: ")

        if choice == "1":
            A = input_matrix("Matrix A")
            print("  Matrix A:")
            print_matrix(A)

        elif choice == "2":
            B = input_matrix("Matrix B")
            print("  Matrix B:")
            print_matrix(B)

        elif choice == "3":
            if A and B and validate(A, B, "add"):
                print("  Result (A + B):")
                print_matrix(addition(A, B))

        elif choice == "4":
            if A and B and validate(A, B, "sub"):
                print("  Result (A - B):")
                print_matrix(subtraction(A, B))

        elif choice == "5":
            if A and B and validate(A, B, "multiply"):
                print("  Result (A x B):")
                print_matrix(multiply(A, B))

        elif choice == "6":
            if A:
                print("  Result (Transpose of A):")
                print_matrix(transpose(A))

        elif choice == "7":
            if A:
                k = int(input("  Scalar value: "))
                print(f"  Result ({k} x A):")
                print_matrix(scalar_multiply(A, k))

        elif choice == "8":
            if A:
                size = len(A)
                if size == 2:
                    print(f"  Determinant: {det_2x2(A)}")
                elif size == 3:
                    print(f"  Determinant: {det_3x3(A)}")
                else:
                    print(" Not Supported !")

        elif choice == "0":
            print("\n  Bye! ")
            break

        else:
            print(" Incorrect Choice.Try again")

menu()
