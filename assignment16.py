num=int(input("Enter one number:"))
rev=0
c=0
k=num
while(num>0):
    a=num%10
    rev=a**3
    num=num//10
    c+=rev
if(c==k):
    print("armstron number")
else:
    print('not armstron number')
