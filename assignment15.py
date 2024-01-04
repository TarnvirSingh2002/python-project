num=int(input("enter one number:"))
k=1
rev=0
a=0
while(num>0):
    a=num%10
    k*=a
    rev+=a
    num=num//10
if(rev==k):
    print('it is a spy number!')
else:
    print("not spy number")