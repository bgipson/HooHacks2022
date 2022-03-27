import time
import board
import RPi.GPIO as GPIO
from adafruit_motorkit import MotorKit

kit = MotorKit(i2c=board.I2C())

def StartDispensing(CanistertoMove, AmountToMove):

    PinStop = 21
    GPIO.setup(PinStop, GPIO.IN)
    try:
        for x in range(AmountToMove):
            input_value_PS = GPIO.input(PinStop)
            
            if input_value_PS == False:
                while input_value_PS == False:
                    input_value_PS = GPIO.input(PinBack)
                    #print("You pressed the Backwards button")
                output = "Stop"
                return output
            
            if(CanistertoMove == 0):
                kit.motor1.throttle = .80
                time.sleep(.5)
                kit.motor1.throttle = 0
                
                time.sleep(.25)
                
                kit.motor1.throttle = -.80
                time.sleep(.5)
                kit.motor1.throttle = 0
                
                time.sleep(.25)
            if(CanistertoMove == 1):
                kit.motor2.throttle = .80
                time.sleep(.5)
                kit.motor2.throttle = 0
                
                time.sleep(.25)
                
                kit.motor2.throttle = -.80
                time.sleep(.5)
                kit.motor2.throttle = 0
                
                time.sleep(.25)
            if(CanistertoMove == 2):
                kit.motor3.throttle = .80
                time.sleep(.5)
                kit.motor3.throttle = 0
                
                time.sleep(.25)
                
                kit.motor3.throttle = -.80
                time.sleep(.5)
                kit.motor3.throttle = 0
                
                time.sleep(.25)
            if(CanistertoMove == 3):
                kit.motor4.throttle = .80
                time.sleep(.5)
                kit.motor4.throttle = 0
                
                time.sleep(.25)
                
                kit.motor4.throttle = -.80
                time.sleep(.5)
                kit.motor4.throttle = 0
                
                time.sleep(.25)

    finally:
        GPIO.cleanup()
