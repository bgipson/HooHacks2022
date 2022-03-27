import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in9b_V3
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import png

#LLibaries for James Motor and User Input
import UserInput
import MotorController
import time

logging.basicConfig(level=logging.DEBUG)

def clamp(val, mi, ma):
    if val > ma:
        val = ma
    if val < mi:
        val = mi
    return val

class EDisplay:
    def __init__(self):
        self.epd = epd2in9b_V3.EPD()
        self.epd.init()
        self.blackBuffer = Image.new('1', (self.epd.height, self.epd.width), 255)
        self.blackDrawer = ImageDraw.Draw(self.blackBuffer)

        self.redBuffer = Image.new('1', (self.epd.height, self.epd.width), 255)
        self.redDrawer = ImageDraw.Draw(self.redBuffer)
        print("FINISHED INITIALIZION")

    def writeBlack(self, text, x, y):
        self.blackDrawer.text((x, y), text)

    def writeRed(self, text, x, y):
        self.redDrawer.text((x,y), text)

    def update(self):
        self.epd.display(self.epd.getbuffer(self.blackBuffer), self.epd.getbuffer(self.redBuffer))

    def fillArea(self):
        self.blackDrawer.rectangle((0, 0, self.epd.height, self.epd.width), 255)
        
    def clear(self):
        self.epd.Clear()

    def end(self):
        self.epd.sleep()


#These Variables will be made but for now they are testing
#With preset ingredients and values
#[0] = Canister 1 and [3] = Canister 4

Canister_Ingredients[4] = ["Salt" , "Pepper", "Chili Powder", "Garlic Powder"]
Canister_Amounts[4] = [1, 2, 4, 12]
Canister_Amounts_MEAS[4] = [0,0,0,0]

for x in range(Canister_Amounts):
    if(Canister_Amounts[x] >=0 and Canister_Amounts[x] < 4):
        Canister_Amounts_MEAS[x] = (Canister_Amounts[x],"/4 tsp")
    elif(Canister_Amounts[x] >=4 and Canister_Amounts[x] < 16):
        Canister_Amounts_MEAS[x] =  (Canister_Amounts[x]/float(4)," tbsp")
    else:
        Canister_Amounts_MEAS[x] =  ("ERROR")

    #May need to do cups and what not
 

try:
    display = EDisplay()
    #switch out spices for variables, do same for amounts-James' count
    display.writeBlack("Spices used: ", 10, 10)
    display.writeBlack((Canister_Ingredients[0]," qty: ", Canister_Amounts_MEAS[x]), 10, 20)
    display.writeBlack((Canister_Ingredients[1]," qty: ", Canister_Amounts_MEAS[x]), 10, 30)
    display.writeBlack((Canister_Ingredients[2]," qty: ", Canister_Amounts_MEAS[x]), 10, 40)
    display.writeBlack((Canister_Ingredients[3]," qty: ", Canister_Amounts_MEAS[x]), 10, 50)

    display.writeBlack("Current spice: ", 170, 10)
    display.writeBlack(Canister_Ingredients[0], 170, 20)
    display.writeBlack(("Measurement: ",Canister_Amounts_MEAS[x]), 170, 30)
    #be sure to update measurements
    display.writeBlack("* Press confirm to dispense all ingredients.", 10, 70)
    display.writeBlack("* Or for selected spice, use buttons below", 10, 100)
    display.writeBlack("to increase/decrease spice amount", 10, 111)
    display.update()
    
    display.end()
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in9d.epdconfig.module_exit()
    exit()

MotorCounter = 0
MaxTeaSpoons = 30

#What Buttons do we need. We can have:
#Confirm - GO
#Increase Selected - Front
#Decrease Selected - Back
#Rotate selected - Toggle
#Cancel Dispension/Back - Toggle(when pressed during GO

#Input Canister Values needs 4 buttons
#After you scan RFID you selcted which canister
#it must not be already in use
#C1 button
#C2 button
#C3 button
#C4 button
#(We may be able to use Front and back to select Canister TBH)
#The button just toggles different when RFID is scanned (lets do that)


#IF RFID_Read=False:
#Current Canister = What Is toggled by toggle button
Current_Canister = 0 #0 in this Case is Canister 1
#CanisterDispension[4] = [0,0,0,0]
#Canister_Amounts[4] = [1, 2, 4, 12]
try:

    while True:
        ButtonPressed = UserInput.input_button_NoRFID()

        if ButtonPressed == "Go":
            MotorController.StartDispensing(MotorCounter)
            #MotorCounter = 0
            #CanisterDispension[4] = [0,0,0,0]
            for x in range(Canister_Amounts):
                MotorController.StartDispensing(x, Canister_Amounts[x])
                time.sleep(1)
                
            Canister_Amounts[4] = [0, 0, 0, 0]
            

        if ButtonPressed == "Back" and MotorCounter > 0:
            #MotorCounter -= 1
            Canister_Amounts[Current_Canister] -= 1
            
        if ButtonPressed == "Front" and MotorCounter < MaxTeaSpoons:
            #MotorCounter += 1
            Canister_Amounts[Current_Canister] += 1

        if ButtonPressed == "Toggle" and Current_Canister < 4:
            Current_Canister += 1
        elif ButtonPressed == "Toggle" and Current_Canister >= 4:
            Current_Canister = 0

    for x in range(Canister_Amounts):
        if(Canister_Amounts[x] >=0 and Canister_Amounts[x] < 4):
            Canister_Amounts_MEAS[x] = (Canister_Amounts[x],"/4 tsp")
        elif(Canister_Amounts[x] >=4 and Canister_Amounts[x] < 16):
            Canister_Amounts_MEAS[x] =  (Canister_Amounts[x]/float(4)," tbsp")
        else:
            Canister_Amounts_MEAS[x] =  ("ERROR")


    try:
        display = EDisplay()
        #switch out spices for variables, do same for amounts-James' count
        display.writeBlack("Spices used: ", 10, 10)
        display.writeBlack((Canister_Ingredients[0]," qty: ", Canister_Amounts_MEAS[x]), 10, 20)
        display.writeBlack((Canister_Ingredients[1]," qty: ", Canister_Amounts_MEAS[x]), 10, 30)
        display.writeBlack((Canister_Ingredients[2]," qty: ", Canister_Amounts_MEAS[x]), 10, 40)
        display.writeBlack((Canister_Ingredients[3]," qty: ", Canister_Amounts_MEAS[x]), 10, 50)

        display.writeBlack("Current spice: ", 170, 10)
        display.writeBlack(Canister_Ingredients[0], 170, 20)
        display.writeBlack(("Measurement: ",Canister_Amounts_MEAS[x]), 170, 30)
        #be sure to update measurements
        display.writeBlack("* Press confirm to dispense all ingredients.", 10, 70)
        display.writeBlack("* Or for selected spice, use buttons below", 10, 100)
        display.writeBlack("to increase/decrease spice amount", 10, 111)
        display.update()
        
        display.end()
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd2in9d.epdconfig.module_exit()

    finally:
        print("done")

finally:
    print("Now Done")
