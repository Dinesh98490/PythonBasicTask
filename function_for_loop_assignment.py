print a softwarica at 10 times
def soft():
    for i in range(10):
        print('sofftwarica', [i])
soft()

sum of a list 
def list():
    a=[1,2,3,4]
    b=0
    for i in a:
        b += i
    print(b)
list()


3. print each character using indexing
def char():
    a=str(input('enter a string: \n'))
    for i in range(len(a)):
        print(a[i],'=',i)
        
char()


4. write a program to display integer from of a list. given list=[1,"a","c",2,3,4]

def integer(list):
    b=[]
    c=[]
    for i in list:
        if type(i) == int:
            b.append(i)
        elif type(i) == str:
            c.append(i)
            
    print(b)
    print(c)
integer([1,'a', 'c', 2,3,4])



5. multiplication of a each element. given list=[4,5,3,2]

def mull():
    list=[4,5,3,2]
    for i in list:
        print(i)
        for j in range(1,11):
            print(i, '*', j, '=', j*i )
            
mull()


6. multiplication table of a given number
def mull():
    num = int(input('enter a number: \n'))
    for i in range(1,11):
        print(num, '*', i, '=', num*i)
        
mull()

7. reverse a list

def list():
   a=[1,2,3,4]
   a.reverse()
   print(a)
list()



8.  given list is [1,2,3,4] but expected output in new list [2,3,4,5]
def lst():
    a=[1,2,3,4]
    a.pop(0)
    a.insert(3,5)
    print(a)
    
lst()

9. given number is prime or not
def prime():
    num = int(input('Enter a number: \n'))
    if num>1:
        for i in range(2,num):
            if num%i == 0:
                print('Not a prime number')
                break
        else:
            print('Prime number')
            
prime()


10. Write a python program to display all the prime numbers within a given range.
def primenumberrange():
    start = int(input('start  a number: \n'))
    end = int(input('end a number : \n'))
    print('the prime numbers numbers start with', start, 'and', end ,'=')
    while start<=end:
        if start >1:
            for i in range(2,start):
                if start%i == 0:
                 break
            else:
                print(start)
        start += 1
    
primenumberrange()
     


11. Python program that accepts a string and calculate the number of digits and letters and space
 
def string():
    a=eval(input('enter a string: \n'))
    digits=0
    letters=0
    space=0
    for i in a:
        if i.isdigit():
            digits += 1
        elif i.isalpha():
            letters += 1
        elif i.isspace():
            space += 1
    print('the no. of digits:', digits, 'no.of letters:', letters, 'no.of space:', space)
string()
            

12. Python program to check the validity of username and password input by user
def username_password():
    c=3
    for i in range(3):
        username = str(input('Enter a name: \n'))
        password = int(input('Enter a password: \n'))
        c = c-1
    
        if username== 'Dinesh' and password == 1234:
            print('you enter a right password and username')
            break
        else:
            print('Try again, You have', c, 'chances left')
            
    else:
        print('Sorry, the exceed limit and back with certain periods of time')
username_password()



13. program to print the given number is odd or even

def odd():
    a = int(input('enter a number: \n'))
    for i in range(1):
        if a%2 == 0:
         print('the number is even')
        else:
         print('the number is odd')
odd()


14. factorial of a given number

def fact():
    a = int(input('enter a number: \n'))
    b =1
    for i in range(1, a+1):
        b *= i
    print(b)
fact()

15. program to check given number is palindrome or not

def palin():
    a = str(int(input('enter a number: \n')))
    reversed = ''
    for i in a:
        reversed = i+ reversed
    if a == reversed :
        print('the number is palindrome')
    else:
        print('the number is not a palindorme')


palin()


16. program to check given number is armstrong or not


def armstrong():
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
armstrong()

17. Python program to check a number is perfect square

def perfectsquare():
    
    import math

    Num = int(input("Enter the Number to check:  \n"))

    root = math.sqrt(Num)
    if int(root + 0.5) ** 2 == Num:
        print(Num, "is a perfect square")
    else:
        print(Num, "is not a perfect square")
        
perfectsquare()


18. python program to check a number is perfect number

def is_perfect_number(number):
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    return divisors_sum == number


def is_perfect_number(number):  
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    return divisors_sum == number


num = int(input("Enter a number: "))
if is_perfect_number(num):
    print(num, "is a perfect number.")
    
else:
    print(num, "is not a perfect number.")
is_perfect_number(6)



19. Print multiplication table of  1,2,3,4,5,6,7,8 

def multiplication():
    for i in range(1,9):
        for j in range(1,11):
            print(i, '*', j, '=', i*j)
        print()
multiplication()
            

20. Given list is lst=[1,2,3,4] but print 1 and 2 only

def lst():
    lst=[1,2,3,4]
    for i in lst:
        if lst == [3,4]:
            print('3 and 4')
       
    else:
            print('1 and 2')
lst()



21. Python program to calculate the sum of all the odd numbers within the given range.

def sumofodd():
    n = int(input('enter a number: \n'))
    sumodd = 0
    for i in range(1, n+1):
        if i%2 != 0:
            sumodd += i
    print(sumodd)

sumofodd()
    


22. Python program to calculate the sum of all the even numbers within the given range.

def sum_of_even():
    n = int(input('enter a number: \n'))
    sumeven = 0
    for i in range(2, n+1):
        if i%2 == 0:
            sumeven += i
    print(sumeven)
        
sum_of_even()


23. Python program to count the space of a given string

def space_of_string():
    a = input('enter a string: \n')
    is_space = 0
    for i in a:
        if i.isspace():
            is_space += 1
    print('the number of space in string in the code is', is_space)
space_of_string()



24. given list is [1,2,3,4] but expected output is [1,8,27,64]

def lst():
    a = [1,2,3,4]
    b=[i**3 for i in a]
    print(b)
lst()
    


25. Multiplication of a list

def multiplication():
    lst =eval(input('enter a number: \n'))
    mul =1
    for i in lst:
        print(i)
        for j in range(1,11):
            print(i, '*', j, '=', i*j)
        

multiplication()


26. Place a break statement in the for loop so that it prints from 0 to 7 only (including 7). Given range(50)

def number():
    for i in range(50):
        print(i)
        if i == 7:
            break
    
number()
    

27. Write a for loop that iterates through a string and prints every letter.

def letters(a):
    for i in a:
        print(i)
letters(str(input('Enter a string: ')))




28. Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". Hint a=["ram","shyam",1,2] expected output:  Hello!ram Hello!shyam

def hello():
    a = ["ram", "shyam",  1, 2]
    for i in a:
        if isinstance(i, str):  
            print('Hello!',i)
        
hello()
    

29. Using a for loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"] expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']

def lst():
    a = ['ram', 'shyam', 1,2]
    dr_a=[]
    for i in a:
        dr_a.append('Dr.'+str(i))
    print(dr_a)
lst()


30. Write a for loop which appends the square of each number to the new list.

def lst(a):
    b=[]
    for i in a:
        b.append(i**2)
    
    print(b)
 
lst([1,2,3,4,5])


31. Write a for loop using an if statement, that appends each number to the new list if it's positive. given lst1=[111, 32, -9, -45, -17, 9, 85, -10]

def positive():
    lst1=[111, 32, -9, -45, -17, 9, 85, -10]
    lst2 = []
    for i in lst1:
        if i > 0:
            lst2.append(i)
    print(lst2)
positive()



32. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. given list=[0,1,2,3,4,5,6]
def lst(a):
    for i in a:
        if i !=3 and i != 6:
            print(i)
lst([0,1,2,3,4,5,6])


33. Write a for loop which appends the type of each element in the first list to the second list.

def types():
    a = ['dinesh', 1, True, 1.0]
    types = []
    for i in a:
        types.append(type(i))
    print(types)

    
types()



34. Use else block to display a message “Done” after successful execution of for loop.
def succesfull_execution():
    a = 'dinesh'
    for i in a:
        print(i)
    else:
        print('Done')
succesfull_execution()



35. Write a while loop statement to print the following series: 
105 98 -------7
def series():

    a = 105
    while a > 7:
        print(a, end=' ')
        a -= 7
    print(a)

series()

36. removal bad characters from the given string. Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n".  Expected output = pythonpython

def removal_character():
    bad_chars = [';', ':', '!', '*']
    string = "py;th*o:n!;py*t*h:o!n"
    for i in bad_chars:
        string = string.replace(i,'')
    print(string)

removal_character()

37. Python program to count the number of even and odd numbers from a series of numbers. 

def odd_even():
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

odd_even() 

38. Given list is lst=[1,2,3,4] but print 1 2 and 4 only

def lst():
    lst = [1,2,3,4]
    for i in lst:
        if i != 3:
            print(i)

lst()


39. Given list is lst=[1,2,3,4] but print 1 and 4 only

def lst(a):
    for i in a:
        if i != 2 and i != 3:
            print(i)
    
lst([1,2,3,4])

40. Given list is [1,2,3,4] but expected output is [1,"a",2,4]

def lst():
    list = [1, 2, 3, 4]
    b = []
    for element in list:
        if element == 3:
            b.append("a")
        else:
            b.append(element)

    print(b)
    

lst()


by using the while loops and function

1. print "softwarica" 10 times 

def soft():
    a='softwarica'
    i=0
    while i<10:
        print(a)
        i = i+1

soft()

2. Sum of a list 

def lst():
    a=eval(input('Enter a number: \n'))
    sum=0
    i=0
    while i<len(a):
        sum +=a[i]
        i +=1
    print('the sum of the list numbers is', sum)

lst()

3. print each character using indexing

def character():
    a=str(input('enter a string: \n'))
    i=0
    while i<len(a):
        print(i, a[i])
        i += 1
    
character()



4. write a program to display integer from of a list. given list=[1,"a","c",2,3,4]

def lst():
    a= [1,2,'a','b',3,4,5]
    i=0
    while i<len(a):
        if isinstance(a[i], int):
         print(a[i])
        i += 1
lst()


5. multiplication of a each element. given list=[4,5,3,2]

def multiplication():
    a=[4,5,3,2]
    i=0
    mull=1
    while i<len(a):
        mull *= a[i]
        i += 1
    print(mull)
multiplication()

6. multiplication table of a given number

def multiplication():
    a=int(input('enter a number: \n'))
    i=1
    while i<=10:
        print(a, '*', i, '=', a*i)
        i +=1
    
multiplication()


7. reverse a list

def reverse_list():
    a=eval(input('enter a number of list: \n'))
    b=[]
    i=0
    while i<len(a):
        b=[a[i]]+b
        i = i+1
    print(b)

reverse_list()



8.  given list is [1,2,3,4] but expected output in new list [2,3,4,5]

def new_list():
    a=[1,2,3,4]
    i=0
    while i<len(a):
        if a[i] == 1:
            a.remove(1)
            a.insert(3,5)
        i=i+1
    print(a)

new_list()


9. given number is prime or not
def prime_number():
    a = int(input('Enter a number: \n'))
    i = 2

    while i < a:
        if a % i == 0:
            print('Not prime number')
            break
        i += 1
    else:
        print('Prime number')
    
            
prime_number()

10. Write a python program to display all the prime numbers within a given range.
def prime_range():
    start = int(input('Enter the start number: \n'))
    end = int(input('Enter the end number: \n'))
    print('The prime numbers between', start, 'and', end, 'are:')
    
    while start <= end:
        if start > 1:
            is_prime = True
            for i in range(2, start):
                if start % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(start)
        start += 1

prime_range()


11. Python program that accepts a string and calculate the number of digits and letters and space
def string():
    a = input('Enter a string: \n')
    no_digit = 0
    no_letter = 0
    no_spaces = 0
    index = 0

    while index < len(a):
        if a[index].isdigit():
            no_digit += 1
        elif a[index].isalpha():
            no_letter += 1
        elif a[index].isspace():
            no_spaces += 1
        index += 1

    print('Number of digits:', no_digit)
    print('Number of letters:', no_letter)
    print('Number of spaces:', no_spaces)
string()


12. Python program to check the validity of username and password input by users

def username_password():
    c = 5
    while c > 0:
        username = input('Enter a username: \n')
        password = input('Enter your password: \n')
        c -= 1
        if username == 'Dinesh' and password == '1234':
            print('You entered the correct username and password')
            break
        else:
            print('You entered the wrong username and password. Attempts left:', c)

    else:
        print('Sorry, the maximum number of attempts exceeded.')

username_password()

13. program to print the given number is odd or even

def odd_even():
    a = int(input('enter a number: \n'))
    i=0
    while  i in range(a):
        if a%2 == 0:
            print('the number is even')
            break
        else:
            print('the number is odd')
            break
    
odd_even()

14. factorial of a given number
def fact():
    a = int(input('Enter a number: \n'))
    fact = 1
    i = 1
    while i <= a:
        fact *= i
        i += 1

    print(fact)

fact()

15. program to check given number is palindrome or not
def palindrome():
    a = str(int(input('Enter a number: \n')))
    reversed_num = ''
    i = len(a) - 1

    while i >= 0:
        reversed_num += a[i]
        i -= 1

        if a == reversed_num:
            print('The number is a palindrome')
            break
    else:
            print('The number is not a palindrome')

palindrome()



16. program to check given number is armstrong or not

def armstrong():
    num = int(input("Enter a number: "))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")

armstrong()

17. Python program to check a number is perfect square

def perfect_square():
    import math

    Num = int(input("Enter the number to check: "))

    root = math.sqrt(Num)
    int_root = int(root + 0.5)
    is_perfect_square = False

    while int_root >= 1:
        if int_root ** 2 == Num:
            is_perfect_square = True
            break
        int_root -= 1

    if is_perfect_square:
            print(Num, "is a perfect square")
    else:
            print(Num, "is not a perfect square")

perfect_square()


18. python program to check a number is perfect number
def is_perfect_number(number):
    divisors_sum = 0
    i = 1

    while i <= number // 2:
        if number % i == 0:
            divisors_sum += i
        i += 1

    return divisors_sum == number


num = int(input("Enter a number: "))
if is_perfect_number(num):
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")




19. Print multiplication table of  1,2,3,4,5,6,7,8 
def multiplication():
    i=1
    while i <9:
        j=1
        while j <11:
            print(i, '*', j, '=', i*j)
            j += 1
        print()
        i += 1
    
multiplication()


20. Given list is lst=[1,2,3,4] but print 1 and 2 only

def lst():
    lst = [1, 2, 3, 4]
    index = 0

    while index < len(lst):
        if lst[index:index+2] == [3, 4]:
            break
        elif lst[index] <= 2:
            print(lst[index])
        index += 1
    else:
        print('1 and 2')

lst()


21. Python program to calculate the sum of all the odd numbers within the given range.

def sum_odd():
    n = int(input('enter a number: \n'))
    sumodd = 0
    i = 1

    while i <= n:
        if i % 2 != 0:
            sumodd += i
        i += 1

    print(sumodd)

sum_odd()


22. Python program to calculate the sum of all the even numbers within the given range.

def even_range():
    n = int(input('enter a number: \n'))
    sumeven = 0
    i = 2

    while i <= n:
        if i % 2 == 0:
            sumeven += i
        i += 2

    print(sumeven)

even_range()


23. Python program to count the space of a given string

def space_string():
    a = input('enter a string: \n')
    is_space = 0
    index = 0

    while index < len(a):
        if a[index].isspace():
            is_space += 1
        index += 1

    print('the number of spaces in the string is', is_space)

space_string()

24. given list is [1,2,3,4] but expected output is [1,8,27,64]

def lst():
    lst=[1,2,3,4]
    b=[]
    i=0
    while i < len(lst):
        b.append(lst[i]**3)
        i += 1
    print(b)
lst()



25. Multiplication of a list

def multilpication():
    lst = [1, 2, 3, 4, 5]  
    result = 1  
    index = 0

    while index < len(lst):
        result *= lst[index]  
        index += 1  

    print(result)  
multilpication()


26. Place a break statement in the for loop so that it prints from 0 to 7 only (including 7). Given range(50)

def loop():
    i=0
    while i<50:
        print(i)
        if i == 7:
            break
        i += 1
loop()

27. Write a for loop that iterates through a string and prints every letter.

def string():
    a=str(input('Enter  a string: \n'))
    i=0
    while i < len(a):
        print(a[i])
        i += 1
string()

28. Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". Hint a=["ram","shyam",1,2] expected output:  Hello!ram Hello!shyam
def name():
    a = ["ram", "shyam",  1, 2]
    index = 0

    while index < len(a):
        if isinstance(a[index], str):
                print('Hello!', a[index])
        index += 1
name()


29. Using a for loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"] expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']
def Dr():
    a = ['ram', 'shyam', 1, 2]
    dr_a = []
    index = 0

    while index < len(a):
        dr_a.append('Dr.' + str(a[index]))
        index += 1

    print(dr_a)

Dr()

30. Write a for loop which appends the square of each number to the new list.
def square():
    a=[1,2,3,4,5]
    b=[]
    i=0
    while i < len(a):
        b.append(a[i]**2)
        i += 1
    print(b)
square()



31. Write a for loop using an if statement, that appends each number to the new list if it's positive. given lst1=[111, 32, -9, -45, -17, 9, 85, -10]
def postive():
    lst1=[111, 32, -9, -45, -17, 9, 85, -10]
    lst2 = []
    i =0
    while i < len(lst1):
        if lst1[i] > 0:
            lst2.append(lst1[i])
        i += 1
    print(lst2)
postive()


32. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. given list=[0,1,2,3,4,5,6]
def lst():
    list = [0,1,2,3,4,5,6]
    i=0
    while i < len(list):
        if list[i] !=3 and list[i] != 6:
         print(i)
        i += 1
lst()


33. Write a for loop which appends the type of each element in the first list to the second list.
def append_first_second():
    a = ['dinesh', 1, True, 1.0]
    types = []
    i=0
    while i < len(a):
        types.append(type(a[i]))
        i +=1
    print(types)

append_first_second()

34. Use else block to display a message “Done” after successful execution of for loop.

def sucessful_code():
    a = 'dinesh'
    i =0 
    while i < len(a):
        print(a[i])
        i += 1
    else:
        print('Done')

sucessful_code()

35. Write a while loop statement to print the following series: 

105 98 -------7
def series():
    a = 105
    i = 0
    while a > 0:
        print(a, end=' ')
        a -= 7
        i += 1

  
series()

36. removal bad characters from the given string. Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n".  Expected output = pythonpython
def removale():
    bad_chars = [';', ':', '!', '*']
    string = "py;th*o:n!;py*t*h:o!n"
    i=0
    while i < len(bad_chars):
        string = string.replace(bad_chars[i],'')
        i += 1
    print(string)
removale()

37. Python program to count the number of even and odd numbers from a series of numbers.  

def even_odd_series():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    count_odd = 0
    count_even = 0
    i = 0

    while i < len(a):
        if a[i] % 2 == 0:
         count_even += 1
        else:
            count_odd += 1
        i += 1

    print(count_even)
    print(count_odd)


even_odd_series()

38. Given list is lst=[1,2,3,4] but print 1 2 and 4 only

def lst():
    lst = [1, 2, 3, 4]
    i = 0

    while i < len(lst):
        if lst[i] == 1 or lst[i] == 2 or lst[i] == 4:
            print(lst[i])
        i += 1


lst()

39. Given list is lst=[1,2,3,4] but print 1 and 4 only
def lst():
    lst = [1,2,3,4]
    i=0
    while i <  len(lst):
        if lst[i] == 1 or lst[i] == 4:
            print(lst[i])
        i += 1

lst()

40. Given list is [1,2,3,4] but expected output is [1,"a",2,4]

def lst():
    list = [1, 2, 3, 4]
    b = []
    i =0 
    while i <  len(list):
        if list[i] == 3:
            b.append("a")
        else:
            b.append(list[i])
        i += 1

    print(b)
    
lst()







        