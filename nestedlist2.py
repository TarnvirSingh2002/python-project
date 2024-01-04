st=[]
i=0
ll=[]
while(i<3):
    str=[]
    k=0
    while(k<3):
        str.append(int(input("enter number:")))
        k+=1
    st.append(str)
    i+=1
print(st)
for i in range(3):
    a=[]
    for j in range(3):
        ll.append(st[j][i])
    a.append(ll)
    
print(a)