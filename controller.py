from car_model import *

car = car()
commands {'forward':car.goForward, 'back':car.goBack, 'left':car.goLeft, 'right':car.goRight}

while(True):
    command = input("Enter Command: ")
    if command == 'forward':
        car.goForward()
    elif command == 'back':
        car.goBack()
    elif command == 'left':
        car.goLeft()
    elif command == 'right':
        car.goRight()
    car.updateVehicle()
