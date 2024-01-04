import re
n='''as far as i remember i only want to be a gangster'''
p=re.findall('i',n)
for  i in p:
    print(i)
