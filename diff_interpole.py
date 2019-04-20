#Interpolation

#difference table problems

c = int(input("How many Elements: "))

x,y = [],[]
for i in range(c):
    x.append(input("Enter x:"))
    y.append(input("Enter y:"))

delta_y = []
for n in range(1,c):
    delta_y.append( float(y[n])-float(y[n-1]) )

delta_2_y = []
for n in range(1,c-1):
    delta_2_y.append( float(delta_y[n])-float(delta_y[n-1]) )

delta_3_y = []
for n in range(1,c-2):
    delta_3_y.append( float(delta_2_y[n])-float(delta_2_y[n-1]) )

delta_4_y = []
for n in range(1,c-3):
    delta_4_y.append( float(delta_3_y[n])-float(delta_3_y[n-1]) )


print("delta_1_y = ",delta_y)
print("delta_2_y = ",delta_2_y)
print("delta_3_y = ",delta_3_y)
print("delta_4_y = ",delta_4_y)
