
import re
'''
exp = ['from: Ngp to Pune','Pune to ngp','from:bombay to pune','banglore to goa']
for i in exp:
    if re.search('from:',i):
        print(i)


#exp=['narayani.ghatwai@gmail.com','piyushdp28@gmail.com','piyush_pande2889@gmail.com','python1 tutorials','hexaware.com']
for i in exp:
    if re.findall('[a-z0-9._]+\@[a-z]+\.[a-z]+',i):
        print(i)


file = open('C:/Users/piyush/Desktop/re_using_file.txt')
for i in file:
    if re.findall('[a-z0-9._]+\@[a-z]+\.[a-z]+',i):
        print(i)



file =open('data.txt')
for i in file:
    if re.findall('[a-z]+\:[a-z0-9.@]+',i):
        print(i)

#split


file =open('data.txt')
for i in file:
    if re.findall('[a-z]+\:[a-z0-9.@]+',i):
        k,v = i.split(':')
        print('key=',k,'value=',v)
        print('=====================================')
        print('keys=',k)
        print('values=',v)
        print('=====================================')
        print(i)
        print('=============================================')
        print('=============================================')
        print('=============================================')
'''

#split-parsing(IMP)

file =open('data2.txt')
#for i in file:
 #   print(i)
'''SPace delimiter
for i in file:
    if re.findall('[a-z]+\s[0-9]{2}\s[a-z0-9._]+\@[a-z]+\.[a-z]+',i):
        name,age,email = i.split(',')
        print('name=',name,'age=',age,'email=',email)
        print(name)
        print(age)
        print(email)
        print('=============================================')
'''


#csv delimiter
for i in file:
    if re.findall('[a-z]+\,[0-9]{2}\,[a-z0-9._]+\@[a-z]+\.[a-z]+',i):
        name,age,email = i.split(',')
        print('name=',name,'age=',age,'email=',email)
        print(name)
        print(age)
        print(email)
        print('=============================================')
