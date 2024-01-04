a=int(input("Enter one side of the triangle:"))
b=int(input("Enter second side of the triangle:"))
c=int(input("Enter third side of the triangle:"))

if(a+b>c and b+c>a and c+a>b):
    print('this is triangle')
else:
    print("this is not triangle")
