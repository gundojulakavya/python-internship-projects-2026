import numpy as np

def input_matrix(name):
    rows = int(input(f"Enter rows of {name}: "))
    cols = int(input(f"Enter cols of {name}: "))

    print(f"Enter elements of {name}:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    return np.array(matrix)

A = input_matrix("Matrix A")
B = input_matrix("Matrix B")

print("\nMatrix A:\n", A)
print("\nMatrix B:\n", B)

try:
    print("\nAddition:\n", A + B)
except:
    print("\nAddition not possible")

try:
    print("\nSubtraction:\n", A - B)
except:
    print("\nSubtraction not possible")

try:
    print("\nMultiplication:\n", np.dot(A, B))
except:
    print("\nMultiplication not possible")

print("\nTranspose of A:\n", A.T)

try:
    print("\nDeterminant of A:", np.linalg.det(A))
except:
    print("\nDeterminant not possible")