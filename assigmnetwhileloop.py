1.print the softwarica 10 times
a='softwarica'
i=0
while i<10:
    print(a)
    i = i+1

sum of a list
a=eval(input('Enter a number: \n'))
sum=0
i=0
while i<len(a):
    sum +=a[i]
    i +=1
print('the sum of the list numbers is', sum)

indexing of the string 
a=str(input('enter a string: \n'))
i=0
while i<len(a):
    print(i, a[i])
    i += 1

 4 write a program to display the integers from the list:[1,2,'a','b',3,4,5]
a= [1,2,'a','b',3,4,5]
i=0
while i<len(a):
    if isinstance(a[i], int): # isinstance fucntion is used to check the values of the list weather it lies or not
        print(a[i])
    i +=1
    
5 write a multiplication of the each elements[4,5,3,2]
a=[4,5,3,2]
i=0
mull=1
while i<len(a):
    mull *= a[i]
    i += 1
print(mull)
    
6 multiplication of a table of a given number
a=int(input('enter a number: \n'))
i=1
while i<=10:
    print(a, '*', i, '=', a*i)
    i +=1
    
7reverse of a list
a=eval(input('enter a number of list: \n'))
b=[]
i=0
while i<len(a):
    b=[a[i]]+b
    i = i+1
print(b)


8.  given list is [1,2,3,4] but expected output in new list [2,3,4,5]
a=[1,2,3,4]
i=0
while i<len(a):
    if a[i] == 1:
        a.remove(1)
        a.insert(3,5)
    i=i+1
print(a)

9 prime number or not
a = int(input('Enter a number: \n'))
i = 2

while i < (a):
    i += 1
    if a % i == 0:
        print('Not prime number')
        break
else:
    print('Prime number')

10. Write a python program to display all the prime numbers within a given range.
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
    
   



