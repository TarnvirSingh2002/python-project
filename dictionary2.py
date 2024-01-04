name={}
for i in range(3):
    k=input("enter name:")
    ele=input("enter data:")
    name.setdefault(k,ele)
n=input("enter name u want to remove:")
print(name)
f=0
for i in name:
    if(i==n):
        f=1
if(f==0):
    print('not found')
if(f==1):
    name.pop(i)
print(name)

    

