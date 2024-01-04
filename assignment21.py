num=int(input("enter one number:"))
rev=0
k=num
while(num>0):
    a=num%10
    rev=(rev*10)+a
    num//=10
print(rev)
print(rev-k)