time=int(input('Enter time from 1 to 12:'))
c=0

ahead=int(input('enter time ahead:'))
c=time+ahead
if(c>12):
    print('your time will be:',c-12," O' clock")
else:
    print(c)