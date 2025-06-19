# to find a real root of a non-linear equation by bisection method using python programming

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eqn=input('enter the equation in x using python syntax:')

def F(x, eqn):
    return eval(eqn)

def f(x):
    return F(x,eqn)

a,b = float(input('enter the first initial guess:')),float(input('enter the second guess:'))

if f(a) * f(b) > 0:
    print(f'No root lies between {a} and {b}.')
else:
    e,N= float(input('enter the error tolerance:')),int(input('enter the maximum number of iterations:'))
    itr = 1
    A= []
    m=[]
    while itr <= N:
        c = (a + b) / 2
        A.append([itr, a, b, c,f(a),f(b), f(c)])
        m.append(c)
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        error = abs(b - a)
        if error < e:
            A = pd.DataFrame(A,columns=['Iteration', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)'])
            print(A.to_string(index=False))
            print(f'The approx, root is: {c} in {itr} iterations with error: {error}')
            break
        
        itr += 1
    if itr > N:
        print(f'Solution does not converge in {N} iterations.')
    
    m=np.array(m)
    x=np.linspace(-5,5,1000)
    plt.plot(x,f(x),color='r',label=eqn)
    plt.axhline(0,0,color='black')
    plt.axvline(0,0,color='black')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.title('Bisection Method')
    plt.scatter(m,f(m))
    for i,val in enumerate(m):
        plt.text(val,f(val),f'{i+1}')
    plt.show()

#  x^2 − cos(x) = 0 