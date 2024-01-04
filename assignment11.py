num=int(input("Enter one number:"))
c=1
t=1
while(t<=num):
    if(t<num):
        print(t,end='*')
    else:
        print(t,end='=')       
    c*=t
    t+=1
print(c)
  