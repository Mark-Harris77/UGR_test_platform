import RPi.GPIO as GPIO
import time

def initalize():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(7, GPIO.OUT)
    servo = GPIO.PWM(7, 50)
    servo.start(0)
    return servo

def finish(servo):
    servo.stop()
    GPIO.cleanup()

def setWheelAngle(servo, angle):
    if (angle > 180) or (angle < 0):
        raise ValueError("Angle value must be between 0 & 180 degrees")
    servo.ChangeDutyCycle(2+(angle/18))
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)

s = initalize()


for i in range(10):
    a = input("Enter angle: ")
    setWheelAngle(s, a)
z
finish(s)