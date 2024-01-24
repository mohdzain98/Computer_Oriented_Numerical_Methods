#!/usr/bin/env python
# coding: utf-8

# In[44]:


import numpy as np
n=5
x=np.array([0,1,2,3,4])
h=x[1]-x[0]
y=np.array([1,11,22,43,75])
z=np.zeros((n,n))
for i in range(n):
    z[i][0]=y[i]

b=[]
mid=int(len(a)/2)
ahead=mid+1
back=mid-1
b.append(x[mid])
while( len(b)<len(x)):
    b.append(x[ahead])
    b.append(x[back])
    ahead=ahead+1
    back=back-1
    
def cdtable():
    for i in range(1,n):
        for j in range(n-i):
            z[j][i]=((z[j+1][i - 1] - z[j][i - 1]))
    return z
z=cdtable()

def xterm(i,value,b):
    pro=1
    for j in range(i):
        pro=pro*(value-b[j])
    return pro

def fact(fac):
    factorial=1
    for i in range(1,fac+1):
        factorial=factorial*i
    return factorial

def formula():
    global a
    a=[]
    for i in range(n):
        d=(n-i)//2
        a.append(z[d][i])
    
    res=0
    for j in range(1,n):
        res=res+(a[j]/(fact(j)*pow(h,j)))*xterm(j,value,b)
    fres=a[0]+res
    return fres

print("The Table is:\n",z)
print("The extracted values of table:",a)
print("The values of x:",b)
value=2.5
fvalue=formula()  
print("The result is:",fvalue)





