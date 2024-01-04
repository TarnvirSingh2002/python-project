num=int(input("enter one number:"))
num1=num
num2=num
def add(num,num2):
    global num1
    if(num2>0):
        if(num2>1):
            print(num,end="+")
        else:
            print(num,end="")
        num=(num*10)+num1
        add(num,num2-1)
add(num,num2)