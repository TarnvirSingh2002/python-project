import os
nm=input("enter name of file:")
name=input("enter the name of file")
if(os.path.isfile(nm)):
    k=open(nm)
    kk=(k.read())
    if(os.path.isfile(name)):        
        l=open(name,'a')
        for i in kk:
            if(i=='a'or i=='e'or i=='i'or i=='o'or i=='u'):
                l.write(i)
    else:
        print("file not found")
    k.close()
    l.close()
else:
    print("file not found!")
    