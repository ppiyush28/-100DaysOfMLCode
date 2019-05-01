
print ("hello")

print ("\n jll")

print ("this is \\\\ double")
print ("there are mountain /\\/\\/\\/\\/\\ ")
print (" \\\" \\\t  \\\npiyush")

#-----------emoji print----
#http://unicode.org/emoji/charts/emoji-list.html#1f600

print ("\U0001F600 \U0001F601  \t \U0001F603 \t \U0001F605")

#numerical cal

print (2+3)

print ("2+3")

number1 = 3
print(number1)

number2 = 3
print(number2)

print (number1 + number2)
print (number1 / number2)
print (number1 // number2)

print (number1 * number2)

print (number1 ** number2)



#function

num1 = int(input ("enter 1st num \t"))
num2 = int(input ("enter 2nd num \t"))
tt = num1 + num2
print (tt)


name ,age = input ("enter name and age ").split()
name ,age = input ("enter name and age ").split(";")
print (name)
print (age)



#average of 3 nums

num1 = int (input("enter num1"))
num2 = int (input("enter num2"))
num3 = int (input("enter num3"))

#num1 num2 num3 = int input("enter nums").split()

avg = (num1 + num2 + num3) / 3
print (avg)


lang = "python"
print (lang[0:2])



name, char = input ("enter name and char : ").split(",")
print (f"length of name  is {len(name)}")
#print (f"char count is  {name.count(char)}")

#case senatitive
print (f"char count is  {name.lower().count(char.lower())}")


name ="        piyush      "
dots = "..........."
print (name + dots)
print (name.lstrip()+dots)
print (name.rstrip()+dots)
print (name.lstrip().rstrip()+dots)

print (name.strip()+dots)

print (name.replace(" ", "") + dots)


#if and if else

age = int (input ("enter age : "))
if age > 18:
    print ("you can vote")
else: 
    print ("you cant vote")
    
    
#wining num and ramdom num

win_num = int (input("enter wining num : " ))
Guess_num = int (input("enter guesss num : " ))

if Guess_num == win_num:
    print ("you won")
else:
    if Guess_num >  win_num:
        print ("too high")
    else:
        if Guess_num < win_num:
            print ("too low")
    
#dummy if

if age > 18:
    pass



#and

age = 18
name = 'abc'

if age == 18 and name == 'abc':
    print("cond is true")
else:
    print("cond is false")
    
#or 

age = 18
name = 'abc'

if age == 18 or name == 'abc':
    print("cond is true")
else:
    print("cond is false")
    


#in keyword
if 'p' in "piyush":
    print("a is therE")

#check empy

name = "abc"
if name:
    print("not empty")
    
    
#loops

i = 1 
while i < 11:
    print("hello word")
    i = i+1    
  
    
#infinite loop

i = 1 
while i < 11:
    print("hello word")


#for loop
for i in range(10) :
    print(f"hello {i}")
    
i=0    
while i < 10:
    if i== 5:
        break
    print(i)

#break    
for i in range (1,11):
    if i == 5:
        break
    print(i)


#contiue  

for i in range (1,11):
    if i == 5:
        continue
    print(i)  
    
    
#randam

import random
random.num


#functions

def add_sum (x,y):
    return x+y

a = add_sum(3,4)
print(a)



def odd_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
print (odd_even(10))



def songs():
    print ("happy songs")

print songs()

def greater(a,b):
    if a > b :
        return a
    else:
        return b
    
num1 = int (input("enter num1"))    
num2 = int (input("enter num2"))         


bigger = greater (num1,num2)
    
print (f"{bigger} num is big")



#polindrom func

def is_polindrom(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False
    
    
print (is_polindrom("naman"))


def is_polindrom(word):
    if word == word[::-1]:
        return True
    else:
        return False
    
    
def is_polindrom(word):
        return word == word[::-1]  



#fibonacci series



#arugment 
def user_info (name,surname,age,add):
    print (f"name is {name} \n")
    print (f"surname is {surname} \n")
    print (f"age is {age} \n")
    print (f"add is {add}")


user_info ("piyush","pande","29","pune")


#list
num=[1,2,3]
num2=[4,7,9]

print(num)
print(num[1])

num.append(6)
#append into last position 

#insert
num.insert(4,7)

#extend 

num.extend(num2)


#pop
num.pop()

num.pop(1)

#del

del num[1]

#remove
num.remove(7) 

word=["pp", "pp1"]
print(word)
print (word[:1])

mixed = [1,2,3,"pp","pp2",2.4]
print (mixed)

mixed[1] = 6
print (mixed)



#split method


user_info = 'piyush 29'.split()
print("user_info")

user_info = 'piyush,29'.split(' , ')
print("user_info")


user_info = ['piyush' , '29']
print (','.join("user_info"))

#loops
#error 
fruits = ["orange","mango","apple"]

for fruit in fruits:
    print(fruits)
    
#while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
    
#error 


#loop inside loop

mat = [[1,2,3],[5,6,7],[8,9,0]] 

print(mat)   
 
for submat in mat:
    for i in submat:
        print(i)
        
        
#range
num = list (range(1,11))        
print (num)

print (num.index(4))


num = [1,2,3,4,6]

def neg_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print (neg_list(num))


#Sqaure of list
def sq_list(l):
    temp = []
    for i in l:
        temp.append(i**2)
    return temp
print(sq(num))

print(sq_list([1,2,3]))


def reverse_num(num):
    num.reverse()
    return(num)

print(reverse_num(num))


num = [[1,2,3],[4,5,6]]

def reverse_num(num):
    
    for i in num:
        i.reverse()
        
    rev=[]
    for i in num:
        for j in i:
            rev.append(j)
    rev.sort()
    rev.reverse()        
    return(rev)

print(reverse_num(num))


#dic

user_info = {'name':'piyush','age':29}
print(user_info)
print(type(user_info))

user1 = dict('name' ='piyush', 'age' = 29}
print(user1)
print(type(user1))


more_info = {'name' : 'piyush pande', 'add':'pune'}
#update
user_info.update(more_info)

#get method

print(user_info.get('name'))


#cude def
for i in a:
    a = {'i':'range(1,10)'}
print(a)
def cude_finder(i):
    temp = {}
    for i in range(1,10):
        temp[i] = i**3
        return temp
print(a)
print (cude_finder(6))


#word count

def word_count(a):
    count = {}
    for char in a:
        count[char]=s.count(a)
        return count
    

print (word_count("piyush"))
#tuple


num = (1,2,3)
print(num)

#tuuple is immutable -- >> num[1]=4

#tuple with  1 element

num = (1,)

print(type(num))


for i in num:
    print(i)



#lambda function 

def add (a,b):
    return a+b

add1 = lambda a,b : a+b


is_even= lambda a : a % 2 == 0
print(is_even(7))
print(is_even(4))


#if else
fucn= lambda s : True if len(s)  > 5 else False
print (fucn('abecsdc'))
  
#no if no but
funct = lambda s : len(s) > 5
print (funct('abecsdc'))


#emurate function 

def find_pos(l,target):
    for pos ,name in enumerate(l):
        if name == target:
            return pos
        return -1
    

print(find_pos(names,"piyush")



#def function ##error -- <function to_power.<locals>.cube at 0x0000001140C16D90>

def to_power(x):
    def cube(n):
        return (n**x)
    return cube

pw = to_power(3)
#cu= cube(2)
print (pw)




#decorator



def deco_funct(funct1):
    def wrap():
        print("this new line")
        funct1()
    return wrap


@deco_funct
def funct1():
    print("this is func1")
    
funct1()    

@deco_funct   
def funct2():
    print("this is fucn2")
    

