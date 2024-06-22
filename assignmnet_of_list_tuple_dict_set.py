1. What will be the output of the following program?
l = [10, 20, 30, 40, 50]
t = ('Sundeep', 25, 79.58)
s = 'set theory'
s1 = set(l)
s2 = set(t)
s3 = set(s)
print(s1)
print(s2)
print(s3)


2.  Given a list
 lst = [10, 25, 4, 12, 3, 8]
 How will you check whether 30 is present in the list or not?
lst=[10,25,4,12,3,8]
for i in lst:
    if i == 30:
        print('You have 30 number inside the loops')
        break
else:
        print('sorry, you don not have a 30 numbers')


3. Write a Python program to unpack a tuple into several variables.
a=('dinesh','kunwar',1,2,3)
first_name, last_name, num1, num2, num3 =a
print(first_name)
print(last_name)
print(num1)
print(num2)
print(num3)


4.  Write a Python program to copy a list
a=[1,2,3,'dinesh']
b=a.copy()
print(b)

5.  Given a string
 s = 'Hello'
 How will you obtain a list['H', 'e', 'l', 'l', 'o'] from it?

s='Hello'
b=list(s)
print(b)


6.  Suppose a list has 20 numbers. Write a program that removes all
 duplicates from this list.

a=[1,2,3,4,5,6,7,8,9,0,0,0,1,1,1,2,3,3,3,3]
b=set(a)
c=list(b)
print(c)


7. Write a Python program to count the number of even and odd numbers from a series of numbers

a=[1,2,3,4,5,6,7,8,9,10]
count_even =0
count_odd = 0
for i in a:
    if i%2 == 0:
        count_even += 1
    else:
        count_odd += 1

print('the number of the even in this series is',count_even)
print('the number of the odd in this series is',count_odd)

8. Write a Python program to add an item in a tuple.

a=('dinesh', 'ram', 1,2,3)
b=list(a)
b.insert(3,'jack')
print(tuple(b))


10.  Write a Python program to convert a tuple to a string.

a=('Hello', 'mate', 'How', 'was','your', 'day?' )
b=' '.join(a)
print(b)


11.  Suppose a list contains positive and negative numbers. Write a
 program to create two lists—one containing positive numbers and
 another containing negative numbers.

a=[-1,2,3,-3,5,-7,-6,-1]
positive_number= []
negative_number=[]
for i in a:
    if i>0:
        positive_number = positive_number + [i]
    else:
        negative_number += [i]

print('postive numbers list:', positive_number)
print('negative number list:', negative_number)


12.  Write a Python program to find the length of a tuple.

a=('dinesh', 'jack', 1,2,3)
print(len(a))


13.  Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}

sample_dictionary = {
    0:10,
    1:20
}
sample_dictionary[2]=30
print(sample_dictionary)

14. Write a Python script to concatenate following dictionaries to create a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
a={
    1:20,
    2:20
}
b={
    3:30,
    4:40
}
c={
    5:50,
    6:60
}
a.update({3:30, 4:40, 5:50, 6:60})
print(a)

15.  Write a Python script to check if a given key already exists in a dictionary.

a={
    'name':'dinesh',
    'class':'bachleor',
    'rollno':14,
    'address':'banke'
}
for i in a.keys():
    if i == 'name':
        print('the keywords are already exist in the dictionary')
        break
else:
    print('sorry keywords are not availble')


16.  Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
a={}
for i in range(1,16):
    a[i]=i**2             #where [i] is the key  and i**2 is the values
print(a) 


17. How will you create a list, tuple, set and dictionary, each containing
 one element?
a=[1]
print(a)
b=(1,)
print(b)
c={1}
print(c)
d={'name':'dinesh'}
print(d)


18. Write a Python program to rename a key in dictionary
a={
    'name':'dinesh',
    'class':'Bachleor',
    'address':'banke'
}
a.pop('name')
a['middle_name']='dinesh'
print(a)


19. Write a Python program to create a set.

a={1,2,3,4,5,6,7,1,13,4}
print(a)

20. Write a Python program to iteration over sets
a={1,2,3,4,5,6,7,'dinesh'}
for i in a:
    if i == 'dinesh':
        print('You found your values')
        break
else:
    print('sorry, the value you searched is not found')


# 21. Write a Python program to add member(s) in a set.

a={1,2,3,4,5,6,7,8}
a.add('dinesh')
print(a)



22. Write a Python program to remove item(s) from set

a={1,2,3,4,5,6,7}
a.discard(6)       # we can also use the remove methods but we don't have right to do indexing in the set and dictioanry
print(a)

23. Write a Python program to remove an item from a set if it is present in the set.

a={1,2,3,4,5,6,'dinesh'}
if 'dinesh' in a:
    a.remove('dinesh')
    print('removed items')
    print(a)
else:
    print('Elemts don'+'t found')

24. Write a Python program to create an intersection of sets.
a={1,2,3,4,5,'dinesh','kunwar', 'bahadur'}
b={9,0,7,6,'dinesh','kunwar', 'bahadur'}
print(a&b) 


25. Write a Python program to update value in dictionary.

a={
    'name':'Dinesh',
    'class':'bachelor',
    'address' : 'banke',
    'height':5.8,
    'college':'softwarica'
}
a['height']=5.9
print(a)


26. Write a Python script to check if a given values exists in a dictionary.

a={
    'name':'dinesh',
    'college':'softwarica',
    'height':5.8
}
for i in a.values():
    if i == 'softwarica':
        print('the value is exist in the program')
        break
        
else:
    print('sorry, the value is not present in the dictionary ')


27. Given the following dictionary:
 d = { 'd1': {'Fruitname' : 'Mango', 'Season' : 'Summer'},
 'd2': {'Fruitname' : 'Orange', 'Season' : 'Winter'}}
 How will you access and print Mango and Winter?
d = { 'd1': {'Fruitname' : 'Mango', 'Season' : 'Summer'},
 'd2': {'Fruitname' : 'Orange', 'Season' : 'Winter'}}
print(d['d1']['Fruitname'])
print(d['d2']['Season'])


28. Given the following dictionary
 marks = {
 'Subu' : {'Maths' : 88, 'Eng' : 60, 'SSt' : 95},
 'Amol' : {'Maths' : 78, 'Eng' : 68, 'SSt' : 89},
 'Raka' : {'Maths' : 56, 'Eng' : 66, 'SSt' : 77}
 }
 Write a program to perform the following operations:
 - Print marks obtained by Amol in English.
 - Set marks obtained by Raka in Maths to 77.

marks = {
 'Subu' : {'Maths' : 88, 'Eng' : 60, 'SSt' : 95},
 'Amol' : {'Maths' : 78, 'Eng' : 68, 'SSt' : 89},
 'Raka' : {'Maths' : 56, 'Eng' : 66, 'SSt' : 77}
}
print('marks botained by the Amol in English : ', marks['Amol']['Eng'])
marks['Raka']['Maths'] = 77
print('updated dictionary: ', marks)



29. How will you create an empty list, empty tuple, empty set and
 empty dictionary?
lst=[1,2,3,4,5]
tple= ()
Set = {1,2,3,4,5}
dic1 = {'dinesh': 12, 'height': 5.8}
lst.clear()
print(lst)
Set.clear()
print(Set)
dic1.clear()
print(dic1)
print(tple)


30. Given dictionary 
a={"salary":20, "age":90}
Write a program to perform the following operations:
-sort the given dictionary by key in ascending order
-sort the given dictionary by value in descending order
a={
    'salary':20,
    'age':90
}
b=sorted(a)
c=[]
for i in a.values():
    c.append(i)
print(b)
print(c)
    
31. Write a program that takes a number.
If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”.
If it is divisible by both 3 and 5, it should return “FizzBuzz”.
Otherwise, it should return the same number.

num = int(input('enter a number: \n'))
if num%5 == 0 and  num%3 == 0:
    print('FizzBuzz')
    
elif num%3 == 0:
    print('Fizz')
    
elif num%5 == 0:
    print('Buzz')
    
else:
    print(num)


32. Given input
a=[1,2,3,4]
expected output: ["ram",1,2,"hari",4]


a=[1,2,3,4]
a.insert(0, 'ram')
print(a)
a[3]='hari'
print(a)



33. Given input
a=[1,2,3,4]
expected output: [1,2,3,4,[8,9]]

a=[1,2,3,4]
a.insert(4,[8,9])
print(a)



