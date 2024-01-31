import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep from time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

ITER_COUNT = 15
pin1 = 13
switch=11

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(switch,GPIO.IN)

try:
    while True:
        if GPIO.input(switch):
            GPIO.output(pin1, GPIO.HIGH)
        else:
            GPIO.output(pin1, GPIO.LOW)
        sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()
