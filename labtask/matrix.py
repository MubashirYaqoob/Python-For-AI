rows = int(input("Rows: "))
cols = int(input("Cols: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"[{i}][{j}] : "))
        row.append(val)
    matrix.append(row)


def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print(f"{val:4}", end=" ")
        print()


print_matrix(matrix)