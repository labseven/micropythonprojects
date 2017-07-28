import lcd
import machine
import time
import socket

print('buttonLCD.py')

oled = lcd.connect()
oled.fill(0)
oled.text("Hi!", 10, 10)
oled.show()

def sendValue(addr, port, value):
    s = socket.socket()
    addr_info = socket.getaddrinfo(addr, port)
    addr = addr_info[0][-1]
    s.connect(addr)
    s.sendall(value)
    s.close()


button = machine.Pin(0, machine.Pin.IN)
lastButtonState = button.value()

while True:
    if button.value() != lastButtonState:
        lastButtonState = button.value()
        if button.value() == False:
            print('button pushed')
            sendValue("labseven.space", 1444, 'Button Pushed')
            oled.fill(1)
            oled.show()
            time.sleep(.1)
            oled.fill(0)
            oled.text(":))))))))))))))", 0, 0)
            oled.text("You're pressing", 0, 10)
            oled.text("my buttons!", 0, 20)
            oled.show()
        else:
            print('button released')
            oled.fill(0)
            oled.show()


    time.sleep(.01)
