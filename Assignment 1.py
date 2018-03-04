
# coding: utf-8

# In[11]:

def Division_by_zero():
    try:
        x = int(input("Enter Number: ") / 0)
    except:
        print ('Division by zero')
    else:
        print (x)
        
Division_by_zero()

