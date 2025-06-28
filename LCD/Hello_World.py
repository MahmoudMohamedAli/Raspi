
# Import modules & setup
#raspi used in this Projetc is Pico

import LCD1602
lcd=LCD1602.LCD1602(16,2)
import time

# Clear the display
lcd.clear()

# Print message at 0,0
lcd.setCursor(0, 0)
lcd.printout("This is Cool!")

#Wait two seconds
time.sleep(2)

# Message from Stanley
lcd.clear()
lcd.setCursor(0, 0)
lcd.printout("Mahmoud says")
lcd.setCursor(0, 1)
lcd.printout("Hello!")