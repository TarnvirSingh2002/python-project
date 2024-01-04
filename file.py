import os
name=input("Enter file name:")
if(os.path.exists(name)):
    f=open(name)
    t=f.read()
    print(t)
    f.close()
else:
    f=open(name,"w")
    f.write("this is a sample data")
    f.close()
