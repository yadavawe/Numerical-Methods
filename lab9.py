import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve

n= int(input('Enter the no. of variables: '))
A=[]
B = []

for i in range(n):
    A.append(list(map(float,input(f'Enter the coefficients of equation {i+1} (space-separated): ').split())))
print(np.matrix(A))

for i in range(n):
    B.append(list(map(float,input(f'Enter the constants: '))))
print(np.matrix(B))

P,L,U= lu(A)
lum = lu_factor(A)
print('Upper triangular matrix U:\n',U)
print('Lower triangular matrix L:\n',L)
print('Permutation matrix P:\n',P)
x = lu_solve(lum,B)
print('Solution:\n',x)
