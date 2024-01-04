num=int(input("enter one number:"))
l=5
k=0
def rev(num):
    global k
    if(num>0):
        rev1=num%10
        k=(k*10)+rev1
        rev(num//10)
    else:
        print(k)
rev(num)
