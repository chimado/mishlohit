import RPi.GPIO as GPIO
import time
import gpiozero
 
delay = 0.0075
degreesToSteps = 7.2
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
# Enable pins for IN1-4 to control step sequence
 
coil_A_1_pin = 5
coil_A_2_pin = 6
coil_B_1_pin = 13
coil_B_2_pin = 19
 
# Set pin states
 
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
 
 
# Function for step sequence
 
def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)


# Rotate clockwise

def stepwise(degrees):
    
    steps = int(degrees / degreesToSteps)
    
    # Loop through step sequence based on number of steps
 
    for i in range(0, steps):
        setStep(1,0,1,0)
        time.sleep(delay)
        setStep(0,1,1,0)
        time.sleep(delay)
        setStep(0,1,0,1)
        time.sleep(delay)
        setStep(1,0,0,1)
        time.sleep(delay)


# Rotate counter clockwise

def stepcounter(degrees):
    
    steps = int(degrees / degreesToSteps)
    
    # Loop through step sequence based on number of steps
 
    for i in range(0, steps):
        setStep(1,0,0,1)
        time.sleep(delay)
        setStep(0,1,0,1)
        time.sleep(delay)
        setStep(0,1,1,0)
        time.sleep(delay)
        setStep(1,0,1,0)
        time.sleep(delay)
    

def main():
    print("done")
    
main()