n={}
for i in range(3):
    k=input("Enter key for dictionary:")
    v=input("enter name:")
    n.setdefault(k,v)
print(n)
l=input("enter name u want to find:")
for i in n:
    if(i==l):
        print(n[i])
