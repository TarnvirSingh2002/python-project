n=''
name=input('enter one name:')
i=len(name)
i-=1
while(i>=0):
    n+=name[i]
    i-=1
print(n)
name=input("enter one name:")
print(name[::-1])

