import lcd_gfx
import writeToLCD as lcd
import time
import machine

pin = machine.Pin(16, machine.Pin.OUT)
pin.value(0)

print("Waiting....")
time.sleep(2)

oled = lcd.connectToDisplay()

r = 1

while True:
    if(r > 120):
        r = 1
        oled.fill(0)
        oled.show()
    lcd_gfx.drawCircle(30, 42, r, oled, 1)
    lcd_gfx.drawCircle(90, 22, r, oled, 1)
    r += 3
    # time.sleep(.05)
