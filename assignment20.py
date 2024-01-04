num=int(input('enter one number:'))
k=0
while(num>0):
    a=num%10
    k+=1
    num=num//10
print(k)
if(k%2==0):
    print('even')
else:
    print('odd')

