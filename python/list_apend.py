list1=[1,2,3,4,5]
list2=[6,7,8,9]
list3=[]
print(list1)
print(list2)
print(list3)
#list3.append(10)
#print(list3)
#list3.append(10,20,30)
#print(list3)
list3.append(list1)
print('list3 after append',list3)
print('length of list3',len(list3))
print(list3[0])
#print(list3[1])
#print(list3[1][:2])
print('===================================================================')
'''
#list extend
list2.extend(list1)
print(list2)
'''
list4=list1+list2
print('list4=list1+list2 ',list4)
print(list1)
list5=list1*3
print('list5=list1*3 ',list5)

for ele in list1:
    print(ele)
#list for loop comprenhsionssa    
print([element for element in list1 if element>3])

