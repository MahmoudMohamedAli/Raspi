import RPi.GPIO as GPIO
import time

# Use BCM numbering
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
LED_PIN = 11              # Pin 11 is GPIO 17

# Setup pin
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on
        time.sleep(1)                    # Wait 1 second
        GPIO.output(LED_PIN, GPIO.LOW)   # Turn off
        time.sleep(1)                    # Wait 1 second
except KeyboardInterrupt:
    print("Stopped by user")
finally:
    GPIO.cleanup()
