st=[]
for i in range(3):
    str=[]
    for k in range(3):
        str.append(int(input('enter number:')))
    st.append(str)
print(st)
for i in range(3):
    kk=0
    for k in range(3):
        kk+=st[i][k]
    print(kk,end=",")
print()
for k in range(3):
    t=0
    for i in range(3):
        t+=st[i][k]
    print(t,end=",")




