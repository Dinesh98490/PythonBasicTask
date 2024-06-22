def login():
    print('hello')
  
login()

parameter and argument are information
def area(l,b):
    print(l*b)
area(10,20)
area(10,10)
area(10,30)

def sum(a,b):
    print(a+b)
sum(1,2)
sum(4,6)

def sum(a,b):
    print(a+b)
sum(20,30)

def mull(a,b):
    print(a*b)
mull(20,30)

def sub(a,b):
    print(a-b)
sub(20,40)
def div(a,b):
    print(a/b)
div(20,40)

repeated parameter is not used in positional argument 
def login(a,b,c):
    print(a,b,c)
login(30,40,60)


def login(name,age):
    print(name,age)
login(40,50,'name=40', 'age=20')

def login(a,b=20):
    print(a,b)
login(10,30)

def add(*a):
    print(a)
add(10,10,10,30,60)

def add(*a,**num):
    print(num,a)
add(50,60,a=30,b=40)

def sum(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)

def div(a,b):
    print(a/b)

def mul(a,b):
    print(a*b)
    
def mod(a,b):
    print(a%b)

sum(1,2)
sub(1,5)
div(2,4)
mul(1,5)
mod(2,2)
mod(4,2)
mod(5,2)



keywords function is used to call the values by the key words
def profile(name,age):
    print(name,age)
profile(name=40,age=50)

return keyword ,namespace,global variable,local variable, and non-local variable

return keywords
def sum(a,b):
   c=a+b
   d=a-b
   return c,d
   
print(sum(10,20))

def sum(a,b):
    return a+b
 
print(sum(10,20))

functions without argument and parameter
def sum():
    a=10
    b=20
    print(a+b)
sum()

functions with argument and paramter
def sum(a,b):
    print(a+b)
sum(10,20)

fucntions with no agrument and with a return values
def sum():
    a=10
    b=20
    return (a+b)
print(sum())

namespace is a collection of names. it is used to avoid the names error
z=30
def add():
    global z
    z=z+2
    a=10
    print(a)
print(z)
add()
print(z)

Enclosed variables
y=20
def add():
    z=30
    def inner():
        nonlocal z
        z=z+5
        a=10
        print(a)
    print(z)
    inner()
    print(z)
add()

legb == local, enclosed, global rules
a=10
def a():
    a=10
    def b():
        a=10
    print(a)
        
    b()
a()

def add(a):
    sum=0
    for i in a:
        sum += i
    print(sum)
add([1,2,3,4])

def python():
    for i in range(10):
        print('softwarica')
python()

def multi():
    for i in range(1,11):
        print(2, '*', i, '=', 2*i)
        
multi()

def rev():
    a=[1,2,3,4]
    a.reverse()
    print(a)
rev()

def add(a,b):
    print(a+b)
    
add(12,12)        
    
def sum(x,y):
    a=x+y
    b=x-y
    return a,b
sub,add=sum(10,10)
print(sub)
print(add)

lambda function    
lambda x,y:x+y
result = lambda n1, n2, n3: n1+ n2+n3
print('sum of the result:', result(12,12,12))

sum = lambda x,y : x+y
print('The sum of the two numbers', sum(12,12))

w=lambda a,b: (a+b, a-b, a/b, a*b)
d,e,f,g=w(10,20)
print(d)
print(e)
print(f)
print(g)

map fucntion used for every elements

a=[1,2,3,4]
b=map(lambda x: x+2, a)
print(list(b))

filter function is used for the filters the data and gives the output to the true values only
a=[1,2,3,4]
b=filter(lambda x: x%2 != 0, a)
print(list(b))

reduce functions
import functools
a=[1,2,3,4]
b=functools.reduce(lambda x,y: x+y, a)
print(b)
 



