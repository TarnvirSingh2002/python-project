my_list=[12,99,46,33,46,129,34,33,122,490,650,700]
t=int(input("Enter number u want to find:"))
k=0
for i in my_list:
    if(i==t):
        k+=1
if(k==0):
    print("not found")
else:
    print(k,"times")