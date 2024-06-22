garbage collection
a=20
a=20
print(a)

slicing
a='dinesh'
print(a[0:3])
print(a[1::2])
print(a[-1:-2])
print(a[-4:-1])
print(a[-1::-2])

casting 
a=str(30)
b=float(20)
c=complex(23)
d=int(23.0)
print(a)
print(b)
print(c)
print(d)

type
a='diensh'
b=23.00
c=True
d=2+3j
print(type(a))
print(type(b))
print(type(c))
print(type(d))

is used for the single line comments and ''' '''  is used for the multi lines comments

python is case sensative such this reason the output will be different and not goes to the garbage collection
the indetifiers start from the A_Z ,a_z not 1 to z, not keywords and not any symbolic signs like $,&,and so on.
A='dinesh'
a=20          # here A and a are different 
print(a)
print(A)

variables name only contain A-Z, a-z and 0-1
when the variables are multi words at that time we used to camel case, pascal case and snake case.
myNameis = 'diensh' # camel case
MyNameIs = 'dinesh' #pascal case
my_name_is ='dinesh' #snake case


many values in the many variables
x,y,z=10,20,30
print(x)
print(y)
print(z)

one value into multi variables
a=b=c= 10
print(a)
print(b)
print(c)

unpack a collection
a=(1,2,3)
x,y,z =a
print(x)
print(y)
print(z)

upper()
a='Hello'
print(a.upper())

#lower()
print(a.lower())
 
strip()
a='      diensh'
print(a.strip())

replace
a='hello'
print(a.replace('h', 'H').replace('o', 'O'))

split()
a='hello'
print(a.split('e'))

capitalize()
a='dinesH'
print(a.capitalize())

centre ()
when the string is in the even form at that time the center value is add to the left 
a='banana'
print(a.center(12, '*'))

a='banana'
print(a.center(13,'0'))

count()
a='dinesh'
b=a.count('i')
print(b)

startswith()
a='pyhton'
print(a.startswith('p'))

endswith()
a='python'
print(a.endswith('n'))

find()
a='dinesh'
print(a.find('e'))

formating is done by the plceholders, keywords or indexing
name='dinesh'
rollno=12
print(f'my name is {name} and my roll no is{rollno}')
print('my name is{} and my roll no is {}'.format(12, 23))
print('my name is {0}and roll no is {1}'.format('dinesh', 23))

isalnum if there is any space or any sybolic values like$,& containing at that time it shows the false value otherwise it always show the true values
a='dinesh123'
b=a.isalnum()
print(b)

isalpha()
a='dinesh'
print(a.isalpha())

isspace() check all the string must be whitespace gives the true otherwise, it gives the false value
a=' '
print(a.isspace())

istitle if the first letter of the string the capital than it gives the true vlaue otherwise, it gives the false values
a='Dinesh Is Good Boy'
print(a.istitle())

join()
a=('diensh','is', 'student')
b=' '.join(a)
print(b)

ljust()
a='banana'
print(a.ljust(20,'*'))

rjust()
b='diensh'
print(a.rjust(20,'&'))
 
partition()
if the value found in the string then it would return the value in the tuple form and gives the string into the middle of the tuple
but the value is not found in the string then it gives the string in the first and then remaining two into the space.
a='dinesh'
print(a.partition('dinesh'))

swapcase()
return the capital value into the small and small to the capital
a='my Name is Tony Stark  '
print(a.swapcase())

zfill()
a='dinesh'
print(a.zfill(9))

boolean values gives the true or false values 
boolean values like[],{},false,() and none gives the fasle values.
a=10
b=20
print(a==b)
print(a>b)
print(b>a)

print(bool([]))
print(bool({}))
print(bool(()))

string formating 
print('my name is {} and i am {} years old'.format( 22,34,56)) # if you put the keywords before the positonal than it gives the error
print('i am a student from {} and which is present in the {}'.format( 21,'ram', 'dinesh','shaym'))
print('my name is tony{0} and i am from the {3}'.format('stark', 'usa', 'canada', 'germany'))


