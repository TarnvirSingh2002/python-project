# n=[]
# i=0
# while(i<10):
#     n.append(int(input("enter one number:")))
#     i+=1
# i=0
# while(i<10):
#     print(n[i])
#     i+=2
#   #another program
n=[]
i=0
t=0
ll=0
kk=0
while(i<10):
    n.append(int(input("enter one number:")))
    i+=1
i=0
while(i<10):
    t=0
    for ii in range(1,n[i]+1):
        if(n[i]%ii==0):
            t+=1
    if(t==2):
        ll+=1
    else:
        kk+=1
    i+=1

print('number of prime numbers',ll)
print('number of non prime numbers:',kk)

