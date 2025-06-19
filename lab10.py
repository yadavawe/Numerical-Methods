#To find the dominant eigenvalue and corresponding vector of a matrix by power method

import numpy as np
import pandas as pd

n=int(input('Enter the order of square matrix: '))
A =[]
for i in range(n):
    A.append(list(map(float,input(f'Enter the square matrix {i+1}th row(space-separated): ').split())))

e,N = float(input('Enter the error tolerance:')),int(input('Enter the maximum no. of iterations: '))
X=[]
for i in range(n):
    X.append(list(map(float,input(f'Enter the coefficients of initial vector: '))))
T = []
itr=1
oldev =0

while itr <=N :
    Y = np.dot(A,X)
    maxev =float(abs(max(Y,key=abs)))
    
    for i in range(n):
        X = Y/maxev
    
    T.append([itr,maxev]+[X[i,0] for i in range(n)])
    err = abs(maxev-oldev)
    
    if err<e:
        break
    oldev = maxev
    itr+=1

if itr>N:
    print(f"The solution does not converge in {N} iterations.")
else:
    T = pd.DataFrame(T, columns= ['iterations','MAXeigenvalue']+[f'x{i+1}' for i in range(n)]).to_string(index= False)
    print(T)
    print(f'Dominant eigenvalue is {maxev} in {itr} iterations')
    print('Corresponding eigenvector is X\n',X)