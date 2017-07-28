import network
from config import wifisettings

def connect(name, passwd):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        print('ssid:', name, 'pass:', passwd)
        sta_if.active(True)
        sta_if.connect(name, passwd)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    return sta_if

def connectOlin():
    connect(wifisettings['ssid'], wifisettings['passwd'])
