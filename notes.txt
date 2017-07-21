Starting micropython:
https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html

esptool is for flashing esp firmware:
sudo pip3 install esptool

List all tty connections:
ls /sys/class/tty/

Erase fw and flash micropython:
sudo esptool.py --port /dev/ttyUSB0 erase_flash
sudo esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170612-v1.9.1.bin

Use picocom or minicom for terminal emulator:
sudo picocom /dev/ttyUSB* -b 115200

To exit picocom:
C-a-x

What fixed connection:
reset a few times after connection, then try enter

sudo ampy --port /dev/ttyUSB* put main.py


boot.py is ran first, then main.py


use mpfshell for uploading files (https://github.com/wendlers/mpfshell):
open ws:


LCDs:
Driven by ssd1306. 128 x 64
Adafruit driver: https://github.com/adafruit/micropython-adafruit-ssd1306
import ssd1306
import machine
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.text("hi", x, y*10)
oled.show()


import writeToLCD as lcd
import lcd_gfx
oled = lcd.connectToDisplay()
lcd_gfx.drawCircle(35, 50, 10, oled, 1)
lcd_gfx.drawFillTrie(63, 50, 63, 20, 50, 20, oled, 1)
