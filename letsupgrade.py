#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assignment 2


# In[ ]:


#question1:

x=int(input ("enter marks"))
if x>=80 and x<=100:
     print("A")
elif x>=60 and x<80:
    print("B")
elif x>=60 and x<70:
    print("C")
elif x>=50 and x<60:
    print("D")
else:
    print("fail")


# In[ ]:


#question2:

from random import randint
x = (1,250)
score=int(input("enter the score"))
if score < 1 and score > 250:
     print("reduce your expectation for 20-20 cricket")
elif score < x:
    print("close by you are true indian fan!")
else:
    print("you dont watch that match!:")


# In[ ]:


#assignment 3


# In[ ]:


file = open("letsupgrade.txt",'w')

file.write("I like cricket")

file.close()


# In[ ]:


file = open("letsupgrade.txt",'r')

print(file.read())

file.close()


# In[ ]:


#assignment4


# L,N,W,H
#how many times want to upload a photo

n = int(input("enter number of chances you want a user to upload? "))

#enter the length size
l = int(input("enter the min length?"))

current_operation = 0
while(current_operation<n):
    current_opeartion += 1
    
    h = int(input("enter your height of photo?"))
    w = int(input("enter your width of photo?"))
    if (h >= 1 and w >= 1):
        if(h==w):
            print("accepted")
        else:
            print("crop it")
    else:
        print("minimum photo size should be -",1)
    
    


# In[ ]:



# assignemnt5


# In[ ]:


ankit_x = 0
ankit_y = 0
max_move = 0
while(max_move <= 5):
    max_move += 1
    command = input("enter the command for ankit to move -")
    command = command.lower()
    
    if(command == "1"):
        ankit_x += -1
    elif(command == "r"):
        ankit_y += +1
    elif(command == "u"):
        ankit_y += 1
    elif(command == "d"):
        ankit_y -= 1
    else:
        print("enter valid input,L,R,U,D")
    print("ankit is here - ", ankit_x, ankit_y)        


# In[ ]:





# In[ ]:




