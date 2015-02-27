#!/usr/bin/python
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import time

LED= "P9_14"
Sensor = "P9_40"

ADC.setup()
GPIO.setup(LED, GPIO.OUT)

while(1):
    Analogreading = ADC.read_raw(Sensor)
    print(str(Analogreading))
    #print(str(CDSvalue))
    time.sleep(.1)
    if Analogreading >= 1:
        GPIO.output(LED, GPIO.HIGH)
    else:
        GPIO.output(LED, GPIO.LOW)
