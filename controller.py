from car_model import *

car = car()
commands {'forward':car.goForward, 'back':car.goBack, 'left':car.goLeft, 'right':car.goRight}


while(True):
    command = input("Enter Command: ")
    if command in commands:
        commands[command]()
        car.updateVehicle()
