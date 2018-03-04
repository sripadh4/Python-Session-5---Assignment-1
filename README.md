# Python-Session-5---Assignment-1

Write a function to compute 5/0 and use try/except to catch the exceptions.

def Division_by_zero():
    try:
        x = int(input("Enter Number: ") / 0)
    except:
        print ('Division by zero')
    else:
        print (x)
        
Division_by_zero()
