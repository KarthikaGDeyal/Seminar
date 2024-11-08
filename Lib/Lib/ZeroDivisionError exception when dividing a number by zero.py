try:
    x=int(input("enter the value of x:"))
    y = int(input("enter the value of y:"))
    result=x/y
    print(result)

except(ZeroDivisionError):
    print("error occured")