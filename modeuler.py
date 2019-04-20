#modified eulers method

def func(x,y):
    return eval(myfunc)

myfunc = input()

def modeuler(x0,xn,y0,h):
    N=0
    x = []
    y = []
    yx = []
    x.append(x0)
    #print(xn,x[0])
    N=int((xn-x[0])/h)

    for i in range(N+1):
        x.append(x[0]+h*(i+1))
        #print(x)

    yx.append(y0)
    y.append(y0)
    print(y)
    
    for n in range(N+1):
        #y[n+1] = y[n] - h*func(x[n],y[n])
        yx.append(y[n] + h*func(x[n],y[n]))
        y.append(y[n] + (h/2)*(func(x[n],y[n])+func(x[n+1],yx[n+1])))
        #print(y[1])
        #print(y,yx)
        #print(y)
        
    return y[N]

print(modeuler(float(input("Enter x[0]:")),
            float(input("Enter x:")),
            float(input("Enter y[0]:")),
            float(input("Enter h:"))
            )
      )
