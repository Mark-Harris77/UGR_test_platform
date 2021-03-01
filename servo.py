import RPi.GPIO as GPIO
import time


#initialize car with values
#return controller to servo object
def initalize():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    servo = GPIO.PWM(7, 50)
    servo.start(0)
    return servo


#finish servo operations
def finish(servo):
    servo.stop()
    GPIO.cleanup()


#set a wheel angle between 0 and 180
def setWheelAngle(servo, angle):
    if (angle > 180) or (angle < 0):
        raise ValueError("Angle value must be between 0 & 180 degrees")
    servo.ChangeDutyCycle(2+(angle/18))
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)

s = initalize()

#test angles
for i in range(10):
    a = float(input("Enter angle: "))
    setWheelAngle(s, a)

#finish test
finish(s)