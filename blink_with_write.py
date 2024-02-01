import RPi.GPIO as GPIO
from time import sleep, strftime

GPIO.setmode(GPIO.BOARD)
LED_PIN = 13
SWITCH_PIN = 11

GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(SWITCH_PIN, GPIO.IN)

blink_rate = float(input("Enter blink rate in seconds (e.g., 1 for 1 second): "))
duration = int(input("Enter how long the program should run in seconds: "))
debug_mode = input("Enable debug mode? (yes/no): ").lower() == 'yes'

import time

start_time = time.time()
iterations = 0

while time.time() - start_time < duration:
    if GPIO.input(SWITCH_PIN) == 1:  # Switch is on
        GPIO.output(LED_PIN, not GPIO.input(LED_PIN))  # Toggle LED
        led_state = "ON" if GPIO.input(LED_PIN) else "OFF"
        
        # Log to file
        with open("data.txt", "a") as file:
            file.write(f"{strftime('%Y-%m-%d %H:%M:%S')}\t{led_state}\n")
        
        # Print debug info if enabled
        if debug_mode:
            print(f"{strftime('%Y-%m-%d %H:%M:%S')}\t{iterations}\t{led_state}")
        
        sleep(blink_rate)
        iterations += 1
    else:  # Switch is off
        if GPIO.input(LED_PIN) != 0:  # Ensure LED is off
            GPIO.output(LED_PIN, GPIO.LOW)
            if debug_mode:
                print(f"{strftime('%Y-%m-%d %H:%M:%S')}\t{iterations}\tOFF")

GPIO.cleanup()

