#!/usr/bin/python
import Adafruit_BBIO.GPIO as GPIO
import time

LED = "P9_16"
Button = "P9_14"

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(Button, GPIO.IN)


while(1):
    print str(GPIO.input(Button))
    if GPIO.input(Button) == 0:
        GPIO.output(LED, GPIO.HIGH)
    
    else:
        GPIO.output(LED,GPIO.LOW)
    time.sleep(1)
if KeyboardInterrupt:
    GPIO.cleanup()
        

    
    
