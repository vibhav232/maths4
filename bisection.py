#bisection method

import random
import math

j = input("Enter the Equation:")

def f(x):
    return eval(j)
    
def bisection(p):
    t,y = [0],[3]

    for i in range(0,4):
        if(f(i)<0):
            t[0]=i
            break
        
    for i in range(0,4):
        if(f(i)>0):
            y[0]=i
            break
    
    total=[float(format(0,'.' + str(int(p)-1) + 'f')+'1')]
    
    i=1
    c = [2]
    while(abs(f(c[0])) > total[0]):
        c = [(float(t[0])+float(y[0]))/2.0]
        
        print(i)
        print(t[0])
        print(y[0])

        print(c[0])
        print("f(0)=",f(c[0]))
        
        if( f(c[0]) < 0 ):
            t[0]=round(c[0],4)
            i+=1
        elif( f(c[0]) > 0):
            y[0]=round(c[0],4)
            i+=1
        else:
            break

    print("Answer is {0:.4f}".format(c[0]))

bisection(input("How many decimal points: "))
