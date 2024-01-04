st=[]
for i in range(3):
    str=[]
    for o in range(3):
        str.append(int(input("enter number:")))
    st.append(str)
for i in range(3):
    for k in range(3):
        if(st[i][k]==st[k][::-1]):
            print(st[i][k])

        

