 1. print "softwarica" 10 times 
for i in range(1,11):
    print('softwarica')
    
2. Sum of a list 

a = eval(input('enter a number: \n'))
sum = 0
if type(a) == list:
    for i in a:
        sum += i
    print('the sum of the integrs', sum)
else:
        print('the number is invalid')


 3. print each character using indexing
a = str(input('enter a number: \n'))
index = 0
for i in a:
    print(i, index)
    index += 1
    
 4. write a program to display integer from of a list. given list=[1,"a","c",2,3,4]

a = [1,'a', 'c', 2,3,4]
for i in a:
    if type(i) == int:
        print(i)


5. multiplication of a each element. given list=[4,5,3,2]

a = [4,5,3,2]
mul = 1
for i in a:
    mul *= i
print(mul)

6. multiplication table of a given number
a = int(input('enter a number: \n'))
mull=2
for i in range(1,11):
    
    print(mull, '*', i, '=', mull*i)


 7. reverse a list
    
a = eval(input('enter a list: \n'))
b=[]
for i in a:
        b = [i]+b
print(b)


8.  given list is [1,2,3,4] but expected output in new list [2,3,4,5]

a =[1,2,3,4]
for i in a:
 if i == 1:
   a.remove(1)
   a.append(5)
print(a)


9. given number is prime or not
prime_number = int(input('enter a number: \n'))

if prime_number>1:
    for i in range(2,prime_number):
     if prime_number % i == 0:

          print('the number is not a prime number')
          break
    
    else:
     print(prime_number,'prime number')

10. Write a python program to display all the prime numbers within a given range.

a = int(input('enter a number: \n'))
initial_values = 2
print(2)
for i in range(initial_values, a):
    if i % initial_values != 0:
        print(i)
    
11. Python program that accepts a string and calculate the number of digits and letters and space  
a = input('enter a number: \n')
no_digit = 0
no_letter = 0
no_spaces = 0
for i in a:
    if i.isdigit():
        no_digit += 1
    elif i.isalpha():
        no_letter += 1
    elif i.isspace():
        no_spaces += 1
print('no. of digit =', no_digit, 'no. of letter = ', no_letter, 'no. of sapces =',  no_spaces)
    
    
12. Python program to check the validity of username and password input by users
c = 5
for i in range(5):
    username = input('enter a username: \n')
    password = input('enter your password: \n')
    c= c-1
    if username == 'Dinesh' and password == '1234':
        print('You entered the right password and username')
        break
    else:
        print('You enter the wrong password and username', c)
        
else:
    print('soory the attempt is exceed')


13. program to print the given number is odd or even

a = int(input('enter a number: \n'))
for i in range(1):
    if a%2 == 0:
        print('the number is even')
    else:
        print('the number is odd')


14. factorial of a given number
a = int(input('enter a number: \n'))
b =1
for i in range(1, a+1):
    b *= i
print(b)


15. program to check given number is palindrome or not
a = str(int(input('enter a number: \n')))
reversed = ''
for i in a:
    reversed = i+ reversed
if a == reversed :
        print('the number is palindrome')
else:
        print('the number is not a palindorme')

16. program to check given number is armstrong or not


num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

 17. Python program to check a number is perfect square
import math

Num = int(input("Enter the Number to check "))

root = math.sqrt(Num)
if int(root + 0.5) ** 2 == Num:
    print(Num, "is a perfect square")
else:
    print(Num, "is not a perfect square")

19. Print multiplication table of  1,2,3,4,5,6,7,8 
a = 1,2,3,4,5,6,7,8
for i in range(1,11):
    print(i, '*',1, '=', i*1)
    print(i, '*', 2, '=', i*2)
    print(i, '*', 3, '=', i*3)
    print(i, '*', 4, '=', i*4)
    print(i, '*', 5, '=', i*5)
    print(i, '*', 6, '=', i*6)
    print(i, '*', 7, '=', i*7)
    print(i, '*', 8, '=', i*8)
    print(i, '*', 9, '=', i*9)
    print(i, '*', 10, '=', i*10)

20. Given list is lst=[1,2,3,4] but print 1 and 2 only
   
lst = [1,2,3,4]
for i in lst:
   if lst == [3,4]:
       print('3 and 4')
       
else:
   print('1 and 2')

21. Python program to calculate the sum of all the odd numbers within the given range.
n = int(input('enter a number: \n'))
sumodd = 0
for i in range(1, n+1):
    if i%2 != 0:
        sumodd += i
print(sumodd)
    
22. Python program to calculate the sum of all the even numbers within the given range.

n = int(input('enter a number: \n'))
sumeven = 0
for i in range(2, n+1):
    if i%2 == 0:
        sumeven += i
print(sumeven)
        
23. Python program to count the space of a given string
a = input('enter a string: \n')
is_space = 0
for i in a:
    if i.isspace():
        is_space += 1
print('the number of space in string in the code is', is_space)

24. given list is [1,2,3,4] but expected output is [1,8,27,64]

a = [1,2,3,4]
b=[i**3 for i in a]
print(b)

25. Multiplication of a list
lst =eval(input('enter a number: \n'))
mul =1
for i in range(1,11):
     print(i,'*',lst,'=', i*lst)

26. Place a break statement in the for loop so that it prints from 0 to 7 only (including 7). Given range(50)

for i in range(50):
    print(i)
    if i == 7:
        print(i)
        break

    
27. Write a for loop that iterates through a string and prints every letter.

a = str(input('enter a string: \n'))
for i in a:
    print(i)


28. Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". Hint a=["ram","shyam",1,2] expected output:  Hello!ram Hello!shyam
a = ["ram", "shyam", 'hari', 1, 2]
for name in a:
    if isinstance(name, str):  
        print('Hello', name)

29. Using a for loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"] expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']
a = ['ram', 'shyam', 1,2]
dr_a=[]
for i in a:
    dr_a.append('Dr.'+str(i))
print(dr_a)
   
30. Write a for loop which appends the square of each number to the new list.
a=[1,2,3,4,5]
b=[]
for i in a:
    b.append(i**2)
    
print(b)

31. Write a for loop using an if statement, that appends each number to the new list if it's positive. given lst1=[111, 32, -9, -45, -17, 9, 85, -10]
lst1=[111, 32, -9, -45, -17, 9, 85, -10]
lst2 = []
for i in lst1:
    if i > 0:
        lst2.append(i)
print(lst2)

32. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. given list=[0,1,2,3,4,5,6]
list = [0,1,2,3,4,5,6]
for i in list:
    if i !=3 and i != 6:
        print(i)


33. Write a for loop which appends the type of each element in the first list to the second list.

a = ['dinesh', 1, True, 1.0]
types = []
for i in a:
    types.append(type(i))
print(types)

34. Use else block to display a message “Done” after successful execution of for loop.
a = 'dinesh'
for i in a:
    print(i)
else:
    print('Done')


35. Write a while loop statement to print the following series: 

105 98 -------7

a = 105
while a > 7:
    print(a, end=' ')
    a -= 7
print(a)


36. removal bad characters from the given string. Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n".  Expected output = pythonpython
bad_chars = [';', ':', '!', '*']
string = "py;th*o:n!;py*t*h:o!n"
for i in bad_chars:
    string = string.replace(i,'')
print(string)

37. Python program to count the number of even and odd numbers from a series of numbers.  
a= [1,2,3,4,5,6,7,8,9,10,11,12,13]
count_odd = 0
count_even = 0
for i in a:
    if i%2 == 0:
        count_even += 1
    else:
        count_odd += 1
print(count_even)
print(count_odd)


38. Given list is lst=[1,2,3,4] but print 1 2 and 4 only
lst = [1,2,3,4]
for i in lst:
    if i != 3:
        print(i)

39. Given list is lst=[1,2,3,4] but print 1 and 4 only

lst = [1,2,3,4]
for i in lst:
    if i != 2 and i != 3:
        print(i)

40. Given list is [1,2,3,4] but expected output is [1,"a",2,4]

lst = [1,2,3,4]
lst[1] = 'a'
del lst[2]
print(lst)



