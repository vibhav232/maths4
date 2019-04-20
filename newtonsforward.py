#newtons fowrward interpolation


c = int(input("How many Elements: "))

x,y = [],[]
for i in range(c):
    x.append(input("Enter x:"))
    y.append(input("Enter y:"))

xn = float(input("Enter x[n]:"))

r= (float(xn)-float(x[0]))/(float(x[1])-float(x[0]))

print(r)

for i in range(c-1):
    y[n+1]-y[n]
