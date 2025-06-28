# Import modules & set things up
import LCD1602
lcd=LCD1602.LCD1602(16,2)
from machine import Pin
import time
lcd.clear()

#Set up switch on GP0, with internal pull-down resistor
switch = Pin(0, Pin.IN, Pin.PULL_DOWN)

#Get game ready
lcd.setCursor(0, 0)
lcd.printout("Hold down switch")
lcd.setCursor(0, 1)
lcd.printout("for 15 seconds")

#Main loop
while True:
    # Wait until switch pressed:
    while switch.value() == 0:
        time.sleep(0.02)
    
    #Game on
    start = (time.time_ns())
    lcd.clear()
    lcd.setCursor(0, 0)
    lcd.printout("Game in play...")
    
    # Wait until switch released
    while switch.value():
        time.sleep(0.02)
        
    #Game end
    elapsed = int((time.time_ns() - start)/1000000000)
    lcd.clear()
    lcd.setCursor(0, 0)
    lcd.printout("That was")
    lcd.setCursor(9, 0)
    lcd.printout(elapsed)
    lcd.setCursor(0, 1)
    if elapsed == 10:
        lcd.printout("Perfect!")
    elif elapsed > 8 and elapsed < 12:
        lcd.printout("Most excellent!")
    elif elapsed > 7 and elapsed < 13:
        lcd.printout("Fair")
    else:
        lcd.printout("Useless!")