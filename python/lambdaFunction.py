from functools import reduce
def add(x,y):
    return x+y

result=add(100,200)
print('result of 100 and 200= ',result)
print('Addition of the add(x,y)',add(10,20))

sum= lambda x,y : x+y
print(sum(120,150))

square=lambda x: x**2
print(square(25))



def addthree(x,y,z):
    return x+y+z

print('Addition of 3 numbers',addthree(10,20,30))


sumthree= lambda x,y,z: x+y+z
print(sumthree(10,20,30))


print('=============================')
list1=[10,20,30,40,50,60,70,80,90]
sqr=(map(lambda x:x**2,list1))
print(list(sqr))
print('============================')

L = [lambda x: x ** 2,lambda x: x ** 3,lambda x: x ** 4]
for f in L:
    print(f(4))
print('===================================')

a = [1,2,3,4]
b = [17,12,11,10]
#c = [-1,-4,5,9]
print(list(map(lambda x,y : x+y, a,b)))
print('========================')

fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x!=1, fib)
print(list(result))

f = lambda a,b: a if (a > b) else b
print(reduce( f, [1, 2, 3, 4, 10,5]))



print(reduce(lambda x,y: x+y, [47,11,42,13]))






