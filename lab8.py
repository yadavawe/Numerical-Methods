# To solve the system of linear equation by Gauss-seidal Method

import numpy as np
import pandas as pd

n = int(input('Enter the no. of variables: '))
A=[]

for i in range(n):
    A.append(list(map(float,input(f"Enter the coefficients of equation {i+1} (space-separated):").split())))
    
A = np.array(A)
print("The augmented matrix is: ")
print(np.matrix(A))

e,N = float(input('Enter the tolerance error: ')),int(input('Enter the maximum no. of iterations: '))

x=[]

for i in range(n):
    x.append(list(map(float,input('Enter the initial values: ').split())))
    
x=np.array(x)
print(np.matrix(x))

itr =1

T=[]
while itr <= N:
    x_old = np.copy(x)
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += A[i,j] * x[j]
        x[i]= (A[i,-1]-s)/A[i,i]
    
    T.append([itr] + [x[i,0] for i in range(n)])
    err = np.abs(x-x_old)
    if np.all(err<e):
        break
    itr+=1

if itr>N:
    print(f'The solution does not converge in {N} iterations.')
    
else:
    T = pd.DataFrame(T, columns= ['iterations']+[f'x{i+1}' for i in range(n)]).to_string(index= False)
    print(T)
    print('The solution is :')
    for i in range(n):
        print(f'x{i+1}={x[i]}')
