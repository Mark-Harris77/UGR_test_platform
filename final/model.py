import RPi.GPIO as GPIO

DRIVE = "PIN NO"
STEER = "PIN NO"
STEERING_MIN = 0
STEERING_MAX = 1


class car:
    def __init__(self):
        self.state = [0,0] #drive, steering
        self.setupGPIO()

    def setDrive(self, val):
        val = min(10, max(-10, val))
        self.state[0] = val

    def setSteer(self, val):
        val = min(10, max(-10, val))
        self.state[1] = val
        
        
    def updateVehicle(self):
        pass



    def setupGPIO(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(DRIVE, GPIO.OUT)
        GPIO.setup(STEER, GPIO.OUT)
        self.driveMotor = GPIO.PWM(DRIVE, 50)
        self.driveMotor.start(0)
        self.steerMotor = GPIO.PWM(STEER, 50)
        self.steerMotor.start(0)

    def cleanup(self):
        self.driveMotor.stop()
        self.steerMotor.stop()
        GPIO.cleanup()
        