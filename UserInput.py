import time
import RPi.GPIO as GPIO




# If button is pushed, light up LED
def input_button_NoRFID():
    pushed = False
    # Pins definitions
    PinBack = 12
    PinFront = 16
    PinGo = 20
    PinToggle = 21
    #Canister_1 = 5
    #Canister_2 = 13
    #Canister_3 = 19
    #Canister_4 = 26

    # Set up pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PinBack, GPIO.IN)
    GPIO.setup(PinFront, GPIO.IN)
    GPIO.setup(PinGo, GPIO.IN)
    GPIO.setup(PinToggle, GPIO.IN)
    #GPIO.setup(Canister_1, GPIO.IN)
    #GPIO.setup(Canister_2, GPIO.IN)
    #GPIO.setup(Canister_3, GPIO.IN)
    #GPIO.setup(Canister_4, GPIO.IN)
    
    output = "Null"
    #pushed = False
    
    try:
        while True:
            input_value_PB = GPIO.input(PinBack)
            input_value_PF = GPIO.input(PinFront)
            input_value_PG = GPIO.input(PinGo)
            input_value_PS = GPIO.input(PinToggle)
            #input_value_C1 = GPIO.input(Canister_1)
            #input_value_C2 = GPIO.input(Canister_2)
            #input_value_C3 = GPIO.input(Canister_3)
            #input_value_C4 = GPIO.input(Canister_4)
            
            
            if input_value_PB == False:
                while input_value_PB == False:
                    input_value_PB = GPIO.input(PinBack)
                #print("You pressed the Backwards button")
                output = "Back"
                return output
                
            if input_value_PF == False:
                while input_value_PF == False:
                    input_value_PF = GPIO.input(PinFront)
                #print("You pressed the Forewards button")
                output = "Front"
                return output
                
            if input_value_PG == False:
                while input_value_PG == False:
                    input_value_PG = GPIO.input(PinGo)
                #print("You pressed the Forewards button")
                output = "Go"
                return output
            
            if input_value_PS == False:
                while input_value_PS == False:
                    input_value_PS = GPIO.input(PinStop)
                #print("You pressed the Toggle button")
                output = "Toggle"
                return output
            
            #if input_value_C1 == False:
            #    while input_value_C1 == False:
            #       input_value_C1 = GPIO.input(Canister_1)
            #  print("You pressed the Canister_1 button")
            # output = "C1"
            #return output
            
            #if input_value_C2 == False:
            #    while input_value_C2 == False:
            #        input_value_C2 = GPIO.input(Canister_2)
            #    print("You pressed the Canister_2 button")
            #    output = "C2"
            #    return output
            
            #Here we look for Canisters
            
    # When you press ctrl+c, this will be called
    finally:
        GPIO.cleanup()
        #return output


def input_button_YesRFID():
    pushed = False
    # Pins definitions
    Canister_1 = 12
    Canister_2 = 16
    Canister_3 = 20
    Canister_4 = 21

    # Set up pins
    GPIO.setup(Canister_1, GPIO.IN)
    GPIO.setup(Canister_2, GPIO.IN)
    GPIO.setup(Canister_3, GPIO.IN)
    GPIO.setup(Canister_4, GPIO.IN)
    
    output = "Null"
    #pushed = False
    
    try:
        while True:
            input_value_C1 = GPIO.input(Canister_1)
            input_value_C2 = GPIO.input(Canister_2)
            input_value_C3 = GPIO.input(Canister_3)
            input_value_C4 = GPIO.input(Canister_4)
            
            if input_value_C1 == False:
                while input_value_C1 == False:
                   input_value_C1 = GPIO.input(Canister_1)
              #print("You pressed the Canister_1 button")
                output = "C1"
                return output
            
            if input_value_C2 == False:
                while input_value_C2 == False:
                    input_value_C2 = GPIO.input(Canister_2)
                #print("You pressed the Canister_2 button")
                output = "C2"
                return output
            
    # When you press ctrl+c, this will be called
    finally:
        GPIO.cleanup()
        #return outputRFID():
    
