there are three methods to add data in the list
1. append .2extend. 3. insert

a=[1,2,3,4]
a[1]=8
print(a)

a=[1,2,3]
a.append(45)
print(a)

a=[1,2,3,4]
a.extend([2,3,'ram'])
print(a)

pop, remove and del
a=[1,2,3,4]
a.pop(1)
print(a)

a=[1,2,3,4]
a.remove(4)
print(a)

a=[1,2,3,4]
del a[0]
print(a)

clear,copy and concatenation
a=[1,2,3,4]
a.clear()
print(a)

copy 
a=[1,2,3,4]
data = a.copy()
print(data)

a=[1,2,3,4,1,1,1]
b=[]
for i in range(len(a)):
    if a[i] == 1:
       b.append(i)
print(b)

tuple values are irreplacebale 
a=(1,2,3,4)
b=list(a)
b.insert(3,5)
print(tuple(b))


set is unchangeable and immutable but it can add the values inside in it.
add
a={'facebook', 'jack', 1,2,3, 'mahesh',1,2}
a.add('dinesh')
print(a)

a={1,2,3,4}
print(a)
a.pop()
print(a)

a={'dinesh',1,2,3,4}
print(a)
a.pop()
print(a)

a={1.00, 'dinesh', 2,3,4,1}
print(a)
a.pop()
print(a)

update the values in any set,tuple, list, etc.
fruits = {'apples', 'pineapples', 'oranges', 'pears'}
fruit= {'grape', 'vegetable', 'gauva'}
fruits.update(fruit)
print(fruits)

here are examples of the add list into the set
a={'dinesh', 'jack', 'harrymaguire', 'cristianio ronaldo'}
b=('oranegs', 'gauva', 'vegetables')
a.update(b)
print(a)

remove 
a={'dinesh', 'harry', 'kane', 'tom'}
a.remove('dinesh')
print(a)

discard 
a={'book', 'pencil', 'copy', 'eraser'}
a.discard('copy')
print(a)

pop  
a={'dinesh', 'jack', 'harry', 'kane'}
a.pop()
print(a)
in this methods we will do not know the which value we want remove, it will simply remove the one values from the set

clear this empty the sets
a={'dinesh', 1,2,3,4}
a.clear()
print(a)

a={1,2,3,4}
a.remove(3)
print(a)



union of the sets
a={'dinesh', 'jack', 'jone', 'krish',1,1,2}
b={1,2,3,4}
c= a|b
print(c)

union and update exclude the any duplicate values

intersection means the gives the result of the duplicate values
a={'dinesh', 1,2,3,4,5,6,7}
b={'dinesh', 1,2,3,4,8,0}
c= a&b
print(c)

symmeteric_difference_update means remove the all duplicate values 
a={1,2,3,0}
b={3,4,5,6}
a.symmetric_difference_update(b)
print(a)

symmetric_difference means the remove all the duplicate values and present the non-dupliacate values 
here True and 1 are read as the same values and False and 0 are the same 
a={True, 'dinesh', 0}
b={1, False, 'jone'}
z=a^b
print(z)

differnce
a={1,2,3}
b={0,4,5,6,3}
c=a-b
print(c)

disjoint
a={1,2,3}
b={4,5,6}
c=a.isdisjoint(b)
print(c)

subset
a={1,2,3,4,5}
b={1,2,3,4,5,6,7,8,9,0}
c=a.issubset(b)
print(c)

superset
a={1,2,3,4,5}
b={1,2,3}
c=a.issuperset(b)
print(c)


dictionary

dictionary={}
print(dictionary)

dictionary={1:'apple', 2:'ball'}
print(dictionary)

a={'name':'ram', 1:[1,2,3]}
print(a)

a = dict({1:'apple', 2:'ball'})
print(a)

a=dict([(1,'apple'), (2,'ball')])
print(a)


a={
    'name':'ram'
}
a['name']='dinesh'
print(a)


a={
    'name':'dinesh'
}
for i in a.keys():
    print(i)


a={
    'name':'dinesh'
}
for i in a.values():
    print(i)



a={
    'name':'dinesh'
}
for i in a.items():
    print(i)


a={'name': 'ram', 'age':20}
c=a.get('name')
print(c)


a={1:2,3:4}
c=a.pop(3)
print(c)


pop items
a={1:2,3:4}
c=a.popitem()
print(c)


a={'name':'ram'}
a.pop('name')
a['hari']='ram'
a[0]='dinesh'
print(a)







a={
    1 : 'januray',
    2 : 'feburary', 
    3 : 'march',
    4 : 'april',
    5:'may', 
    6: 'june', 
    7: 'july', 
    8:'august',
    9:'september',
    10:'october',
    11:'november',
    12: 'december'
}
print(a[7])

keys are key values in the dictionary
a={
    'name' : 'dinesh',
    'middle_name' : 'bahadur',
    'last_name' : 'kunwar',
    'D_O_B' : 2001,
    'address' : 'banke',
    'level' : 'bachelor',
    'height' : 5.10,
}
a['height']=5.6
print(a)
items values return the tuples
a={
    'a' : 'mustang', 
    'b' : 'ford', 
    'c':'porsche',
    'd':'mercedes',
    'e' : 'BMW',
    'f':'lamborgaini'
}
print(a.items())
if 'e' in a:
    print('Yes, the code is sucessfully')

update methods to update the values of the dictionary only if you pass the key values
a={
    'name':'Dinesh',
    'DOB' : 2001,
    'color' : 'red'
}
a.update({'name' : 'kunwar'})
print(a)


there are two ways values to add in the dictionary  update
a={
    'name':'dinesh',
    'last_name': 'kunwar',
    'calss' : 'bachelor',
    'roll_no':'unknown',
    'height' : 5.8
}
a.update({'middle_name':'bahadur'})
print(a)



a=100
b=50
print(a and b)
print(10%6)
print(2**3**2)


print(-10//4)
print(0b101)
a=' diensh'
print(a.isalnum())
a='dinesh'
b='dinesh'
print(a==b)
print(a is b)
a= 'dinesh'
print(a.isalnum())
a='900'
print(a.isdigit())
