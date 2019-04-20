#Runge-Kutta method

def func(x,y):
    return eval(myfunc)

myfunc = input()

def RK(x0,y0,xn,h):
    k = [0,0,0,0,0]
    x,y = [],[]
    x.append(x0)
    y.append(y0)

    N = int((xn-x0)/h)

    for n in range(N+1):
        x.append(x[n]+h)

    print(x)

    for n in range(N+1):
        for i in range(5):
            if(i == 1):
                k[1] = h*func(x[n],y[n])
                #print(k[i])
            elif(i==2 or i==3):
                k[i] = h*func(x[n]+h/2,y[n]+k[i-1]/2)
                #print(k[i])
            elif(i==4):
                k[4] = h*func(x[n]+h,y[n]+k[i-1])
                #print(k[i])

        y.append(y[n] + (k[1]+2*k[2]+2*k[3]+k[4])/6)

    print(y)
    return y[N]

print(RK(float(input("Enter x[0]:")),
         float(input("Enter y[0]:")),
         float(input("Enter x:")),
         float(input("Enter h:"))
         )
      )
