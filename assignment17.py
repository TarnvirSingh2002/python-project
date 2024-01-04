n=int(input('enter one number:'))
m=int(input("enter another number:"))
a=0
k=0
while(m<=n):
    if(m%2==0):
        a+=m
    elif(m%2!=0):
        k+=m
    m+=1
print("sum of even number is:",a)
print("sum of odd number is:",k)