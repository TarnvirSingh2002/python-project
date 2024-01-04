years=[2018, 1963, 2014,2005, 1966,2010,1970,2005,1974,2005,1982,1996,1984]
years.remove(2005)
years.append(1987)
for i in years:
    if(i==2005):
        years.remove(i)
years.sort()
print(years)
