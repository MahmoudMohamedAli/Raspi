# Import modules & set things up
import LCD1602
lcd=LCD1602.LCD1602(16,2)
from machine import Pin
import time
lcd.clear()

#Set up switch on GP0, with internal pull-down resistor
switch = Pin(0, Pin.IN, Pin.PULL_DOWN)

#Set value of counter to zero & output to LCD
counter = 0
lcd.setCursor(0, 0)
lcd.printout("Count is ")
lcd.setCursor(9, 0)
lcd.printout(counter)

while True:
    while switch.value():
        counter = counter + 1
        lcd.setCursor(9, 0)
        lcd.printout(counter)
        while switch.value():
            time.sleep(0.1)
    time.sleep(0.1)