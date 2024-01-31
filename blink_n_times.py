import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep from time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

ITER_COUNT = 0
pin1 = 13
pin2=11

GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)

input_value=input('how many blinks')
if input_value == "":
        n = 5
else:
        n = int(input_value)

GPIO.setup(pin2,GPIO.IN)
while not GPIO.input(pin2):
	GPIO.output(pin1,GPIO.LOW)


if n>0:   
	ITER_COUNT = n
	
	while ITER_COUNT > 0: # Run ITER_COUNT times
                ITER_COUNT -= 1 # Decrement counter
                GPIO.output(pin1, GPIO.HIGH) # Turn on
                sleep(1)                     # Sleep for 1 second
                GPIO.output(pin1, GPIO.LOW)  # Turn off
                sleep(1)
else :
	ITER_COUNT = 5
	pin1 = 13


	while ITER_COUNT > 0: # Run ITER_COUNT times
   		ITER_COUNT -= 1 # Decrement counter
   		GPIO.output(pin1, GPIO.HIGH) # Turn on
   		sleep(1)                     # Sleep for 1 second
   		GPIO.output(pin1, GPIO.LOW)  # Turn off
   		sleep(1)                     # Sleep for 1 second
	GPIO.cleanup()
