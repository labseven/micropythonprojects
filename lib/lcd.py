import ssd1306
import machine

def connect():
    pin = machine.Pin(16, machine.Pin.OUT)
    pin.value(0)
    i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)
    return oled
