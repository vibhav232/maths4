#taylors series method

#how to do differentiation !!!! help!!!!!!!!!!!!!!!!!!!!!!!



from sympy import *

def func(x,y):
    return eval(myfunc)

def fun(a):
    if a <= 0:
        return 1
    else:
        return a*fun(a-1)

myfunc = input()

def taylor(x0,y0,xn,h):
    x,y = [],[]
    x.append(x0)
    y.append(y0)
   
    N = int((xn-x0)/h)

    for n in range(N+1):
        x.append(x[n]+h)

    for i in range(6):
        (func(x,y))  *(h**i)/fun(i)     ##help here plz
        
        
    return p[N]

print(taylor(float(input("Enter x[0]:")),
         float(input("Enter y[0]:")),
         float(input("Enter x:")),
         float(input("Enter h:"))
         )
      )
