#program to executes division and handles an arithmetic error exception if there is an arithmetic error
try:
    x=int(input("enter the value of x:"))
    y = int(input("enter the value of y:"))
    result=x/y
    print(result)

except(ArithmeticError):
    print("error occured")

