l=[]
for i in range(3):
    f=[]
    for ii in range(3):
        c=int(input("enter one number:"))
        f.append(c)
    l.append(f)
print("you unique unique numbers are:")
u=[]
for i in l:  
    for ii in i:
        if ii not in u:
            u.append(ii)
print(u)
for i in u:
    print(i)
# l=[]
# for i in range(12):
#     c=int(input("enter one number:"))
#     l.append(c)
# k=[]
# for i in l:
#     if i not in k:
#         k.append(i)
# for i in k:
#     print(i)