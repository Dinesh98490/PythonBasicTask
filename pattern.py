make a pattern for the A 
for row in range(7):
    for column in range(4):
        if(column == 0) and (row != 0) or (column == 1)and (row == 0) or (row == 4) or (column==2) and (row==0 or row==4) or(column==3) and (row !=0) :
            print('*', end='')
        else:
            print(end=' ')
    print()

this code make the M pattern
for row in range(6):
    for column in range(5):
        if(column == 0)or (column == 1) and (row ==2 ) or(column == 2)and(row == 3)or (column ==3)and(row == 2)or(column ==4):
            print('*', end='')
        else:
            print(end=' ')
    print()        


this code for the make the b pattern 
for row in range(7):
    for cloumn in range(4):
        if (cloumn == 0)or(cloumn == 1)and (row == 0 or row == 3 or row == 6) or (cloumn == 2) and (row == 0 or row == 3 or row == 6) or (cloumn == 3) and (row != 0 and row !=6):
            print('*', end='')
        else:
            print(end =' ')
    print()

make a pattern for the c 

for r in range(6):
    for c in range(4):
        if (c==0) and (r!=0 and r!=5) or (c==1) and(r==0 or r==5) or (c==2) and (r==0 or r ==5) or (c==3) and(r ==0 or r==5):
            print('*', end='')
        else:
            print(end=' ')
            
    print()

make a pattern for the D letters
for row in range(6):
    for column in range(4):
        if(column==0) or (column == 1) and (row ==0 or row == 5) or (column == 2) and (row==0 or row ==5) or (column==3) and(row !=0 and row !=5):
            print('*', end='')
        else:
            print(end=' ')
            
    print()

make a pattern for the E alphabet letters 
for row in range(7):
    for column in range(4):
        if(column == 0) or (column==1) and (row == 0 or row == 3 or row == 6) or(column == 2) and (row == 0 or row == 3 or row == 6) or (column==3) and (row == 0 or row == 3 or row == 6):
            print('E', end='')
        else:
            print(end= ' ')
    print()

make a pattern for the F letters 
for row in range(7):
    for column in range(4):
        if (column == 0) or (column==1) and (row == 0 or row == 3) or (column ==2) and (row == 0 or row == 3) or (column == 3) and(row == 0 or row == 3):
            print('F', end='')
        else:
            print(end=' ')
    print()

make a pattern for  the G letters 
for row in range(7):
    for column in range(4):
        if (column == 0)and (row != 0 and row != 6) or (column== 1) and(row==0 or row == 6) or (column ==2) and(row==0 or row == 4 or row == 6) or (column ==3) and(row !=1 and row != 2 and row != 3):
            print('G', end='')
        else:
            print(end='  ')
    print() 
            
make a pattern for the H letters in alphabet 
for row in range(7):
    for column in range(4):
        if (column ==0) or (column ==1 ) and (row ==3) or (column == 2) and (row==3) or(column == 3):
            print('H', end='')
        else:
            print(end=' ')
    print()

make a pattern for the I letters for alphabet
for row in range(7):
    for column in range(5):
        if(column == 0) and (row == 0 or row ==6) or(column == 1) and (row == 0 or row == 6) or (column == 2) or (column == 3) and (row == 0 or row == 6) or (column == 4) and (row == 0 or row == 6):
            print('I', end='')
        else:
            print(end=' ')
    print()

make a pattern for the J letters for alphabet
for row in range(7):
    for column in range(4):
        if (column == 0) and (row == 5 or row == 6) or (column==1) and (row == 0 or row == 6) or (column == 2) or (column == 3) and (row == 0):
            print('J', end='')
        else:
            print(end=' ')
    print()


print a pattern for the K letters 
for row in  range(7):
    for column in range(4):
        if (column == 0) or (column == 1) and (row== 2 or row == 4) or (column == 2) and (row==1 or row == 5) or (column == 3) and (row == 0 or row ==6):
            print('K', end='')
        else:
            print(end =' ')
    print()


print a pattern for the L letters
for row in range(6):
    for column in range(4):
        if (column ==0) or (column == 1) and(row ==5) or (column == 2) and (row == 5) or (column == 3) and (row ==5):
            print('*', end ='')
        else:
            print(end =' ')
            
    print()



                              