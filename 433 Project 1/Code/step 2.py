import RPi.GPIO as GPIO 
from time import sleep 
import time 

'''
    This is the code for step 2 of project 1. 
    We were tasked with creating a circuit with 2 buttons 
    and 2 LEDs. 
    One LED was to blink at varying time intervals, unless a button was pressed to put it at constant interval.  
    The other LED was to blink at varying brightness. 

    One button changed the LED behavior and the other button 
    was to change which LED's behavior would be changed. 
'''

#GPIO pins
blueLED = 18 
greenLED = 12   
changeButtonOut = 16 #power to the change function button
changeButtonIn = 18 #input from the change function button
functButtonOut = 22 #power to the do function button
functButtonIn = 24 #input from the do function button

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) #use physical PIN numbers
#lights are on by default
GPIO.setup(blueLED, GPIO.OUT, initial=GPIO.HIGH) 
GPIO.setup(greenLED, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(changeButtonOut, GPIO.OUT, initial=GPIO.HIGH)#output power to button
GPIO.setup(changeButtonIn, GPIO.IN)
GPIO.setup(functButtonOut, GPIO.OUT, initial=GPIO.HIGH) #output power to button
GPIO.setup(functButtonIn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

startTime = time.time()
pwm = GPIO.PWM(12, 1000)
pwm.start(25) #start at 25% brightness
#Blink speeds are in an array to make the change speed funciton easier. 
blinkSpeeds = [.25, .5, 1] #possible blink speeds. How many seconds per blink
currentSpeed = 0 #this is an index of the blinkspeeds array
constSpeed = False #are we at constant blink speed?
isBlue = True #is the function affecting the blue LED (ie is it blink speed?)
pwmBright = 25
def changeSpeed(): #changes blinkspeed
    global currentSpeed #index of current speed in blinkSpeeds. 
    #increment, and go back to 0 if out of bounds. 
    currentSpeed += 1 
    currentSpeed %= len(blinkSpeeds)

while True: 
    if(GPIO.input(functButtonIn)): 
        if isBlue:
            constSpeed = not constSpeed #switch constSpeed. 
        else: #changes between 25% brightness and full brightness
            if pwmBright == 25: 
                pwmBright = 100
            else:
                pwmBright = 25
            pwm.ChangeDutyCycle(pwmBright)
        print("pushed") #prints message to console
    if(GPIO.input(changeButtonIn)): 
            isBlue = not isBlue #swap blue.
            print("Function changed") #prints message to console
    if(time.time() - startTime> 4 and not constSpeed): #changes blink speed every 4 seconds if not on constant speed
            changeSpeed()
            startTime = time.time()
    #blinks
    GPIO.output(blueLED, GPIO.LOW)
    sleep(blinkSpeeds[currentSpeed])
    GPIO.output(blueLED, GPIO.HIGH) 
    sleep(blinkSpeeds[currentSpeed])
    print(currentSpeed)#prints blink speed 


