import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time

servo= "P8_13"
Pot = "P9_40"

ADC.setup()
PWM.start(servo,0, 50)

#while(1):
    
#    Command = raw_input("Servo read? (r/x):")
#    if Command == 'r':
while(1):
            Potreading = ADC.read(Pot)
            servoPos = ((Potreading * 5) + 5 )
 #       print("Potentiometer:")
            print(str(servoPos))
            PWM.set_duty_cycle(servo, servoPos)
 #           time.sleep()

#            if KeyboardInterrupt:
 #               PWM.stop(servo)
 #               PWM.cleanup()
  

#if Command == 'x':
#        print("Program end")
#        PWM.stop("P8_13")
#        PWM.cleanup()
#        exit()


   # Potreading = ADC.read(Pot)
#    print(str(Potreading))
#    time.sleep(1)
    
