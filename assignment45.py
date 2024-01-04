n=[]
i=0
k=0
j=0
while(i<10):
    n.append(int(input("enter number:")))
    i+=1
i=0
while(i<10):
    if(n[i]%2==0):
        k=k+n[i]
    else:
        j+=n[i]
    i+=1
print('sum of all even numbers:',k)
print('sum of all odd numbers',j)
