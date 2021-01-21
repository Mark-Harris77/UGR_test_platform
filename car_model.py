import RPi.GPIO as GPIO




class car:
    FORWARD = 26
    BACK = 6
    LEFT = 13
    RIGHT = 19
    def __init__(self):
        self.state = [0,0,0,0]#forward, back, left, right
        setupGPIO()
        
    def goLeft(self):
        self.state[3] = 0
        self.state[2] = 1
        

    def goRight(self):
        self.state[2] = 0
        self.state[3] = 1
    
    def goForward(self):
        self.state[1] = 0
        self.state[0] = 1

    def goBack(self):
        self.state[0] = 0
        self.state[1] = 1
    
    def stop(self):
        self.state = [0,0,0,0]
        
    def updateVehicle(self):
        state = self.state
        if state[0] == 1:
            GPIO.output(FORWARD, GPIO.HIGH)
        else:
            GPIO.output(FORWARD, GPIO.LOW)
        if state[1] == 1:
            GPIO.output(BACK, GPIO.HIGH)
        else:
            GPIO.output(BACK, GPIO.LOW)
        if state[2] == 1:
            GPIO.output(LEFT, GPIO.HIGH)
        else:
            GPIO.output(LEFT, GPIO.LOW)

        if state[3] == 1:
            GPIO.output(RIGHT, GPIO.HIGH)
        else:
            GPIO.output(RIGHT, GPIO.LOW)


    def setupGPIO():
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)