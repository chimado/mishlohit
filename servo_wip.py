# imports
import RPi.GPIO as GPIO
import time
import gpiozero

# GPIO library setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# pins
test_pin = 12

# setup
GPIO.setup(test_pin, GPIO.OUT)
pwm=GPIO.PWM(test_pin, 50)
pwm.start(0)

# functions
def servo(angle):
    duty = angle / 18 + 2
    GPIO.output(test_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(test_pin, False)
    pwm.ChangeDutyCycle(0)

# main code

def main():
    servo(0)
    time.sleep(1)
    servo(90)
    time.sleep(1)
    servo(180)
    
main()
pwm.stop()
GPIO.cleanup()
print("done")
