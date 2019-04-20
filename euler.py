def func(x,y):
    return eval(fun)

fun = input()

def euler(x0,xn,y0,h):
    N=0
    x = []
    y = []
    x.append(x0)
    #print(xn,x[0])
    N=int((xn-x[0])/h)

    for i in range(N):
        x.append(x[0]+h*(i+1))
        #print(x)

    y.append(y0)
    
    for n in range(N+1):
        #y[n+1] = y[n] - h*func(x[n],y[n])
        y.append(y[n] + h*func(x[n],y[n]))
        #print(y)
        
    return y[N]

print(euler(float(input("Enter x[0]:")),
            float(input("Enter x:")),
            float(input("Enter y[0]:")),
            float(input("Enter h:"))
            )
      )
