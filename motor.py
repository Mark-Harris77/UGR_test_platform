import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
motor = GPIO.PWM(7,50)

motor.start(0)
wait = input("connect power")
motor.ChangeDutyCycle(50)
wait = input("Wait for beep")
motor.ChangeDutyCycle(10)
wait = input("Wait for beep")

motor.changeDutyCycle(30)

time.sleep(4)
