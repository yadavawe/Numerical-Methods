# to find a real root of a non-linear equation by Newton-Raphson Method using python programming

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

h = 1e-10
eqn = input("Enter the equation: ")

def F(x, eqn):
    return eval(eqn)

def f(x):
    return F(x, eqn)

def g(x, h):
    return (f(x + h) - f(x)) / h

a = float(input("Enter your guess: "))

if g(a, h) == 0:
    print('Please choose another guess, the derivative is zero at this point.')

else:
    e, N = float(input("Enter the error tolerance :")), int(input("Enter the max number of iterations :"))
    itr = 1
    A = []

    while itr <= N:
        b = a - (f(a) / g(a, h))
        er = abs(b - a)
        A.append([itr, a, f(a), g(a, h), b, f(b), er])

        a = b
        
        if er < e:
            A = pd.DataFrame(A,columns=['Iteration', 'a', 'f(a)', "f'(a)", 'b', 'f(b)', 'Error'])
            print(A.to_string(index=False))
            print(f'The approximate root of the equation is {b} in {itr} iterations')
            break
        
        itr += 1
    if itr > N:
        print(f'The solution does not converge in {N} iterations.')

    pd.set_option('display.float_format', '{:.6f}'.format)
    
    x=np.linspace(-5,5,1000)
    plt.plot(x,f(x),color='r',label=eqn)
    plt.axhline(0,0,color='black')
    plt.axvline(0,0,color='black')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.title('Newton-Raphson Method')
    plt.scatter(b, f(b), color='blue')
    plt.show()