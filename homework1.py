a=eval(input("enter one number:"))
rev=0
while(a>0):
    c=a%10
    rev=(rev*10)+c
    a//=10
print(rev)