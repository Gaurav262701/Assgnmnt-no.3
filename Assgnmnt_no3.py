#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Answer no.1
num = float(input("Enter the number:"))
if num > 0:
    print("its a positive number")
    
elif num == 0:
    print("its a zero")
    
else:
    print("its a negative number")


# In[ ]:


#Answer no.2
num = float(input("Enter the number:"))
if (num % 2) == 0:
    print("its a even number")
    
else:
    print("its a odd number")


# In[ ]:


#Answer no.3
year = int(input("Enter the year:"))
if (year % 400 == 0) and (year % 100 == 0):
    print("its a leap year")
    
elif (year % 4 == 0) and (year % 100 !=0):
    print("its a leap year")
    
else:
    print("its not a leap year")


# In[2]:


#Answer no.4
num = int(input("enter the number:"))
if num>1:
    for i in range(2,(num//2)+1):
        if(num%i==0):
            print(num,"is not a prime number")
            break
            
        else:
            print(num,"is a prime number")
else:
    print(num,"is not a prime number")
    


# In[5]:


#Answer no.5
var_a = 1
var_b = 10000
print("prime number between",var_a,"and",var_b,"are:")
for num in range(var_a,var_b + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
    


# In[ ]:




