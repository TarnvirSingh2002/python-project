a=int(input("Enter one number:"))
t=0
for i in range(1,a+1):
    if(a%i==0):
        t+=1

if(t==2):
    print(a," is prime")
else:
    print(a," is not prime")