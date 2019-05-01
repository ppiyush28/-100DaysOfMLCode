dict1={'name':'piyush', 'age' : 25}
print(dict1)
print(dict1['name'])
print(dict1['age'])
dict1['name']=['piyu','naru','shehal']
print(dict1)

#dic iteration
for item in dict1:
    print(item,dict1[item])

for item in dict1.items():
    print(item)

for key,value in dict1.items():
    print('key is ',key,', value',value)

print(dict1.items())
print(dict1)


city = {'home town':'nagpur','work place':'pune','tour place':'mumbai'}
print(city)

# 1st method update=merge
print('original dict',dict1)
dict1.update(city)
print('updated dict',dict1)

#
print(dict1.keys())

#
print(dict1.values())

#
city.clear()
print('dict after clear fun',city)

#

print(dict1.get('age'))

#
print(dict1)
dict1.popitem()
print('after pop dict1:',dict1)

#keys
print('before pop',dict1)
dict1.pop('name')
print('after pop',dict1)


#copy

new_dict=city.copy()
print('new dcit=',new_dict)
