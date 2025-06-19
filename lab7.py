""" To solve the system of linear equations by gauss jordan with partial pivoting
using python programming"""

import numpy as np

n=int(input('enter the number of variables'))
A=[]
for i in range (n):
    A.append(list(map(float,input(f'Enter the elements in {i+1}th row from enter').split())))

A= np.array(A)
print('The augmented matrix is A=')
print(np.matrix(A))   

for i in range (n):
        p_row=np.argmax(np.abs(A[i:,i]))+i
        A[[i,p_row]]=A[[p_row,i]] 
        
        print(np.matrix(A))
       
        for j in range (i+1,n):
            if j!=i:
                A[j]=[j]-A[j,i]*A[i]
        A[i,:]  /=A[i,i] #normalise
        print (f"Row {i+1} after eliminaton is:" )   
        print(np.matrix (A))
        
        
        


x=A[:,-1] # extraction of solution
    
print('the solution of the matrix is:')
print(x)