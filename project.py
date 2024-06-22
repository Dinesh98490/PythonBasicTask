# The display shows the number of car parking in the building
def carparkingdisplay():
 max_capacity = 200
 for i in range(1,11):
    carparked = int(input('press 1 for parking: \n'))
    if carparked == 1 :
        print('the no.of car parkinng is', i)
        print('maximum capacity is 200')
    else:
        print('sorry, space is not available for parking')

    
carparkingdisplay()