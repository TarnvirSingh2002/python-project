start=int(input("enter one number:"))
step_by=int(input("enter one more number:"))
stop=int(input("enter one more number:"))
print('your start is ',start)
print('your step_by is ',step_by)
print('your stop is ',stop)
c=step_by
while(step_by>0):
    print(start)
    start+=c
    step_by-=1
print(stop)