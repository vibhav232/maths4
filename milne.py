#milne's predictor corrector method

def func(x,y):
    return eval(fun)

fun = input()

def milne(x0,y0,x1,y1,x2,y2,x3,y3,xn):
    N=0
    x = [x0,x1,x2,x3]
    y = [y0,y1,y2,y3]
    yp = [0,0,0,0,0,0]
    yc = [0,0,0,0,0,0]
    
    f = [0]
    
    h = x[1]-x[0]
    N=int((xn-x[0])/h)

    for i in range(4,N+1):
        x.append(h*i)
    
    for n in range(1,N+1):
        if(n <= 3):
            f.append(func(x[n],y[n]))
            if(n==3):
                yp[n+1] = y[n-3]+4*(h/3)*(2*f[n-2]-f[n-1]+2*f[n])
                
        elif(n == 4):
            f.append(func(x[n],yp[n]))
            if(n==4):
                n=3
                yc[n+1] = y[n-1]+(h/3)*(f[n-1]+4*f[n]+f[n+1])
                n=4
            f[n] = func(x[n],yc[n])

#yc[n+1] = y[n-1]+(h/3)*(f[n-1]+4*f[n]+f[n+1])
  
    return yc[N]

print(milne(float(input("Enter x[0]:")),
            float(input("Enter y[0]:")),
            float(input("Enter x[1]:")),
            float(input("Enter y[1]:")),
            float(input("Enter x[2]:")),
            float(input("Enter y[2]:")),
            float(input("Enter x[3]:")),
            float(input("Enter y[3]:")),
            float(input("Enter x[n]:"))
            )
      )
