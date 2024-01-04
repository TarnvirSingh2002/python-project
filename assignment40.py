line=input('enter one line:')
k=""
choice=input("enter your choice:")
if(choice=='F'):
    for i in range(len(line)):
        if(i==0):
            print(line[0])
        if(line[i]==' '):
            print(line[i+1])
if(choice=='L'):
    for i in range(len(line)):
        if(line[i]==" "):
            print(line[i-1])
        if(i==len(line)-1):
            print(line[len(line)-1])

        