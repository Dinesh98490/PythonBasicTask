for r in range(6):
    for c in range(33):
        if (c== 0) and (r == 0 or r ==5) or (c == 1) and(r == 0 or r == 5) or (c==2) or (c==3)and (r ==0 or r ==5)or(c==4):
            print('*', end='')
        elif(c==6) and (r == 0 or r== 5) or (c==7) and(r==0 or r == 5) or (c==8)or (c==9) and(r == 0 or r ==5) or (c==10) and(r==0 or r==5):
            print('*', end ='')
        elif (c==12) or (c==13) and(r==1) or (c==14)and(r==2)or(c==15)and(r==3)or(c==16)and(r==4)or(c==17):
            print('*', end='')
        elif (c==19) or(c==20)and(r==0 or r == 3 or r ==5) or (c==21) and(r==0 or r ==3 or r ==5) or (c==22)and (r==0 or r ==3 or r ==5):
            print('*',end='')
        elif (c==24) and(r !=3 and r !=4) or (c==25) and(r==0 or r ==2 or r ==5)or (c==26) and(r==0 or r==2 or r ==5)or (c==27)and (r!=1):
            print('*', end='')
        elif (c==29) or(c==30)and(r==3) or(c==31)and(r==3) or (c==32)and(r==3)or(c==32):
            print('*',end='')
        else:
            print(end = ' ')
    print()