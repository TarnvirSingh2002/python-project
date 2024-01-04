name=[1,4,76,8,1,34,6,1]
'''print(name)
name[1]="Navjot"
name.append("pawanpreet")
print(name.index(76))
print(name.count(1))
d=name.copy()
name.insert(1,"jatin")
print(name.pop())
#print(d)'''
print(name.pop(4))
name.remove(8)
name.reverse()
name.sort()
print(sum(name))
name.clear()
for i in name:
    print(i)
