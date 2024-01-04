name=input("enter a string:")
ch=input("enter one character:")
def char(name,ch):
    y=0
    for i in range(len(name)):
            if(name[i]==ch):
                y+=1
    print("your character:",y)
char(name,ch)