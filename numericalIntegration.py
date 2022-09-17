#!/usr/bin/env python
# coding: utf-8

# In[7]:


#trapezoidal rule

import math
n=4
a=1
b=2
h=(b-a)/n
x=[]
f=[]
sum=a
x.append(sum)
while (max(x)!=b):
    sum=sum+h
    x.append(sum)

for i in range(n+1):
    f.append(round(math.sqrt(1+(n*math.pow(x[i],2)))*math.sin(x[i]),2))
    
def trapezoidal(f,n,h):
    s=0
    for i in range(1,n):
        s=s+2*f[i]
    res=round((h/2)*round(s+f[0]+f[n],3),4)
    return res

print("x values:",x)
print("f values:",f)
res=trapezoidal(f,n,h)
print("approx value of trapezoidal:",res)


# In[14]:


#simpson1/3
from scipy.integrate import quad
import math

def approx(h,f):
    print(f)
    s1=0
    s2=0
    for i in range(1,n,2):
        s1 +=(f[i])
    s1=round(s1*4,3)

    for i in range(2,n,2):
        s2 +=2*f[i]
    
    res=round((h/3)*(f[0]+f[n]+s1+s2),3)
    return res
appsim=approx(h,f)
print("approx value of simpson1/3:",appsim)

def exact(x):
    res=math.sqrt(1+4*math.pow(x,2))*math.sin(x)
    return res

integral,err=quad(exact,1,2)
print("exact value calculated : ",round(integral,5))



# In[15]:


#simson3/8
def appsim38(h,f):
    s1=0
    s2=0
    for i in range(1,n):
        if(i%3==0):
            s1+=2*f[i]
        else:
            s2+=3*f[i]
    s1=round(s1,3)
    s2=round(s2,3)
    res=round(((3*h)/8)*(f[0]+f[n]+s1+s2),3)
    return res

app=appsim38(h,f)
print("approx value of sim3/8:",app)
print("exact value calculated:",round(integral,3))  
            


# In[16]:


errorinsim=abs(integral-appsim)
errorintrap=abs(integral-res)
errorinsim38=abs(integral-app)
print("error in trapezoidal:",round(errorintrap,8))
print("error in simpson1/3 :",round(errorinsim,8))
print("error in simpson3/8 :",round(errorinsim38,8))


# In[34]:


#GuassQuadrature
#x=mt+c
a=2
b=4
m=(b-a)/2
c=(a+b)/2
t=1/math.sqrt(3)
def fun(x):
    f=(math.sqrt(1+x**2))*(math.exp(-x))
    return f
def phi(t,m,c):
    x=m*t+c
    f=(m*fun(x))
    return f

res=phi(t,m,c)+phi(-t,m,c)
print("approx value :",round(res,4))

def exact(z):
    ret=math.sqrt(1+math.pow(z,2))*math.exp(-z)
    return ret

evalue,err=quad(exact,2,4)
print("exact value  :",round(evalue,4))

error=abs(evalue-res)
print("error : ",round(error,7))


# In[ ]:




