name=input("enter one word:")
k=0
n=""
for i in name:
    k+=1
k-=1

while(k>=0):
    n=n+name[k]
    k-=1
if(n==name):
    print('paledrome')
else:
    print('not paledrome')