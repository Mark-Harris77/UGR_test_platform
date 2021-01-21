from car_model import *

car = car()

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
    elif command == 'stop':
        car.stop()
    car.updateVehicle()
