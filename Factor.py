def Factorial (x):
    """ Hello, my name is Jash."""
    if x==0 or x==1:
        return 1
    else:
        return x*Factorial(x-1)
    
print(Factorial.__doc__)
print (Factorial(5))