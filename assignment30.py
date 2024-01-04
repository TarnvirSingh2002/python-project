num=int(input("enter one number:"))
cc=1
bb=0
while(num>0):
    a=num%10
    c=a
    cc*=c
    b=a
    bb+=b
    num//=10
print(cc+bb)

