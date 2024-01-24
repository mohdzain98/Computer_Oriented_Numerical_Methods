n=int(input("enter the number of points")) #number of points for interpolation
x=[]
y=[]
print("enter the x values and than y values")
for i in range(0,n):
    a=float(input("x {} value".format(i)))
    b=float(input("y {} value".format(i)))
    x.append(a)
    y.append(b)

flag=0
for i in range(0,n-1):
    if(x[i]>x[i+1]):
        flag=1
        break;
if (flag==1):
    for i in range(0,n-1):
        for j in range(0,n-1):
            if(x[j]>x[j+1]):
                x[j],x[j+1]=x[j+1],x[j]
u=float(input("enter the point of interpolation")) 

p=0
if(u<x[0] or u>x[n-1]):
    print("the value must lie between {} to {}".format(x[0],x[n-1]))

else:
    for i in range(0,n):
        k=1
        for j in range(len(x)):
            if(j!=i):
                k=k*(u-x[j])/(x[i]-x[j])
        p=p+(k*y[i])
    print(p)

