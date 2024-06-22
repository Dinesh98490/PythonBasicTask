a='python'
i = 0
while i<6:
    print(i,a[i])
    i = i+1

i=10
j=2
while i>=1:
    print(j,'*',i, '=', i*j)
    i=i-1

factorial number for the any values
a=int(input('enter a number: \n'))
fact=1
i=1
while i<=a:
    fact=fact*i
    i=i+1
print(fact)

this is used for the revverse number and palindrome number
a = str(input('enter a number:\n'))
b=len(a)
i=0
reversed = ''
while i<b:
    reversed = a[i]+reversed
    i=i+1
print(reversed)
if reversed == a:
    print('the number is the palindrome string')
else:
    print('the number is not the palindrome string')

a=int(input('enter a number: \n'))
i=2
while i<a:
    if(a%i == 0):
         i = i+1
         print('Not a prime number')
           
                
   
else:
    print('prime number')
a=int(input('enter a number: \n'))
i=1
j=2
while i<a:
    if i>2:
        if i%j == 0:
            print(i,'Not prime number')
            i=i+1
    else:
        print(i, 'prime number')
