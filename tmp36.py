#!/usr/bin/python
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import time

sensor_pin = 'P9_40'
LED = 'P8_3'

ADC.setup()
GPIO.setup(LED, GPIO.OUT)

while(1):
    reading = ADC.read(sensor_pin)
    millivolts = reading * 1800
    temp_c = (millivolts - 500) / 10
    temp_f = (temp_c * 9/5) +32
    print('mv=%d C=%d F=%d' % (millivolts, temp_c, temp_f))
    time.sleep(1)
    
    if (millivolts >= 625):
        GPIO.output(LED, GPIO.HIGH)
        print("High")
