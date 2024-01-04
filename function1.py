p=int(input("enter one number:"))
k=1
def factorial(p):
    global k
    if(p==0):
        return 0
    else:
        k*=p
        factorial(p-1)
        return k
print(factorial(p))