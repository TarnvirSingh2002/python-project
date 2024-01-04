name=input("enter a string:")
k=0
for i in name:
    k+=1
k-=1
while(k>=0):
    print(name[k],end="")
    k-=1