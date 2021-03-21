# imports
import RPi.GPIO as GPIO
import time
import gpiozero
import numpy as np

# GPIO library setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# pins
in_pin = 23
out_pin = 24

# variables
timing = 0.01

# setup
GPIO.setup(in_pin, GPIO.IN)
GPIO.setup(out_pin, GPIO.OUT)


# arduino coms
def get_input():
    inp = np.zeros(20)
    ver = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
    acc = 0
    
    while acc != 10:
        GPIO.output(out_pin, 1)
        time.sleep(0.01)
        GPIO.output(out_pin, 0)
        time.sleep(0.001)
        
        for i in range(20):
            inp[i] = GPIO.input(in_pin)
            time.sleep(timing)
            
        inp = np.flip(inp, 0)
        print(inp)
    
        for i in range(10):
            if ver[i] == inp[i + 10]:
                acc = acc + 1
                
        acc = 0
    
    return inp
    

# functions
def get_distance():
    return get_input()

# main code
def main():
    print(get_distance())
    
main()
GPIO.cleanup()