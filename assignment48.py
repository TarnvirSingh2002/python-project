name=[]
i=0
while(i<10):
    name.append(input('enter names:'))
    i+=1
i=0
while(i<10):
    if((name[i][0]=='a'or name[i][0]=='e' or name[i][0]=='i' or name[i][0]=='o'or name[i][0]=='u' )and(name[i][-1]=='a'or name[i][-1]=='e' or name[i][-1]=='i' or name[i][-1]=='o'or name[i][-1]=='u' )):
        print(name[i])
    i+=1
