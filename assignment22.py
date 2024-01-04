num=int(input('enter one number:'))
a=0
for i in range(num):
    a+=i
    if(i<num-1):
        print(a,end=",")
    else:
        print(a,end='')


