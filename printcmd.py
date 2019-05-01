'''name='Piyush'
last='Pande'
print(name,last)
print('%s %s'%(name,last))
print(('name={},last name={}').format(name,last))


##sets
#+++++++++++++++++++++++++++++++++++++++
s={10:1,20:2,30:3}
type(s)
print(type(s))
s=set(s)
print(s)
print(type(s))
s.add(40)
print(s)
s.remove(40)
print(s)
s.pop()
print(s)
s.clear()
print(s)



s1=(10,20,30,40)
s2=(30,40,50,60)
s1=set(s1)
s2=set(s2)
print('s1=',s1)
print('s2=',s2)
print('Intersection',s1&s2)
print('Union',s1|s2)
print('Symmetric Difference',s1^s2)
print('Difference',s1-s2)
print('s1<=s2',s1<=s2)
print('s1>=s2',s1>=s2)

'''

s1=(10,20,30,40)
s2=(10,20,30,40,30,40,50,60)
s1=set(s1)
s2=set(s2)
print('s1=',s1)
print('s2=',s2)
print('Intersection',s1&s2)
print('Union',s1|s2)
print('Symmetric Difference',s1^s2)
print('Difference',s1-s2)
print('s1<=s2',s1<=s2)
print('s1>=s2',s1>=s2)

