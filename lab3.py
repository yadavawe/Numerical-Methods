# to find a real root of a non-linear equation by Secant Method using python programming

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eqn=input("Enter the equation: ")
def F(x,eqn):
    return eval(eqn)

def f(x):
    return F(x,eqn)


a=float(input("Enter the first initial guess a: "))
b=float(input("Enter the second guess b:"))
if f(a)==f(b):
    print(f'The solution is not found since {f(a)}={f(b)}')
else:
    e,N=float(input("Enter the tolerance error: ")),int(input("Enter the max no of iterations: "))
    itr=1
    A=[]
    m=[]
    while(itr<=N):
        c=(a*f(b)-b*f(a))/(f(b)-f(a))
        er = abs(c-b)
        
        A.append([itr,a,b,c,f(a),f(b),f(c), er])
        m.append(c)
        a=c
        if er<e:
            A = pd.DataFrame(A,columns=['Iteration', 'a', 'b','c', 'f(a)', 'f(b)','f(c)', 'Error'])
            print(A.to_string(index=False))
            print(f'The approximate root of the equation is {b} in {itr} iterations')
            break
        a,b=b,c
        itr+=1
    if itr>N:
        print(f'The solution does not converge in {N} iterations.') 
    
    pd.set_option('display.float_format', '{:.6f}'.format) 

    m=np.array(m)
    x=np.linspace(-5,5,1000)
    plt.plot(x,f(x),color='r',label=eqn)
    plt.axhline(0,0,color='black')
    plt.axvline(0,0,color='black')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.title('Secant Method')
    plt.scatter(m,f(m))
    for i,val in enumerate(m):
        plt.text(val,f(val),f'{i+1}')
    plt.show()