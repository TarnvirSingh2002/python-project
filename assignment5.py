temperature=float(input("Enter the temperature in Celsius:"))
if(temperature<-273.15):
    print("INVALID")
if(temperature==-273.15):
    print("temperature is absolute 0")
if(temperature>-273.15 and temperature<0):
    print("below freezing")
if(temperature==0):
    print("freezing")
if(temperature>0 and temperature<100):
    print("normal range")
if(temperature==100):
    print("boiling")
if(temperature>100):
    print("above the boiling") 