# Import modules & setup: NB LCD1602.py must be on Pico
import LCD1602
lcd=LCD1602.LCD1602(16,2)
from machine import Pin
import time
lcd.clear()
lcd.setCursor(0, 0)
lcd.printout("Measuring speed!")

#Set up sensor on GP28, note all resistors are on control board
sensor = Pin(28, Pin.IN)

# Anamometer vane diameter (set to the value for your cup-to-cup in mm)
vane_diameter = float(106)

# Calculate vane circumference in metres
vane_circ = float (vane_diameter/1000)*3.1415

# Set an anamometer factor to account for inefficiency (value is a guess)
afactor = float(2.5)

while True:
    # Measurement loop; initially define variables . . .
    rotations = 0 # Was float(0)
    trigger = 0
    endtime = time.time() + 10
    # Get initial state of sensor
    sensorstart = sensor.value()
    # Measurement loop to run for 10 seconds
    while time.time() < endtime:
        if sensor.value() == 1 and trigger == 0:
            rotations = rotations + 1
            trigger = 1
        if sensor.value() == 0:
            trigger = 0
        time.sleep(0.001)
    if rotations == 1 and sensorstart == 1:
        rotations = 0
    # Calculate stuff - windspeed in MPH!
    rots_per_second = float(rotations/10)
    windspeed = round(float((rots_per_second)*vane_circ*afactor*2.237),2)
    # Outout result
    lcd.clear()
    lcd.setCursor(0, 0)
    lcd.printout("Windspeed in MPH:")
    lcd.setCursor(0, 1)
    lcd.printout(str(windspeed))
    time.sleep(1)
