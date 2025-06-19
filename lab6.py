#to solve the system of linear equations by Gauss-Jordan method using python programming

import numpy as np

n = int(input("Enter the number of variables: "))
A = []

for i in range(n):
    row = list(map(float, input(f"Enter coefficients for equation {i + 1} (space-separated): ").split()))
    A.append(row)
    
A = np.array(A)
print("The augmented matrix is:")
print(np.matrix(A))

for i in range(n):
    p_row = np.argmax(np.abs(A[i:, i])) + i
    A[[i, p_row]] = A[[p_row, i]]  # Swap rows
    print(np.matrix(A))
    
    for j in range(n):
        if j != i:
            factor = A[j, i] / A[i, i]
            A[j, :] -= factor * A[i, :]
            
    A[i, :] /= A[i, i]  # Normalize the pivot row
    print(f"Row {i + 1} after elimination: ")
    print(np.matrix(A))
    
x = A[:, -1]  # Extract the solution
print("The solution is:")
print(x)


 #  Enter the number of variables: 4
 #  Enter coefficients for equation 1 (space-separated): -3 1 1 1 0
 #  Enter coefficients for equation 2 (space-separated): 2 -1 3 2 6
 #  Enter coefficients for equation 3 (space-separated): 1 3 -1 1 4
 #  Enter coefficients for equation 4 (space-separated): 4 -1 2 -1 4