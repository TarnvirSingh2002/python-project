phone=0
name=''
name1=''
phone1=0
i=0
while(i<3):
    name=input("enter your name:")
    phone=int(input("Enter your phone number:"))
    i+=1
choice=input("enter name u want to find:")
while(i>3):
    if(name1[i]==choice):
        print(name1[i])
        print(phone1[i])
    i+=1