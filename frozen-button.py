import RPi.GPIO as GPIO
import time
import pyautogui as py
#import Xlib

#class g:
#    xDisplay = "192.168.43.22:0.0"
py.FAILSAFE = False
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(8,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(10)== GPIO.HIGH:
        print("Left Click")
        py.press('space')
        time.sleep(0.3)
    elif GPIO.input(8)== GPIO.HIGH:
        print("Right Click")
        #py.click(button='right')
        time.sleep(0.3)
        
    
    
