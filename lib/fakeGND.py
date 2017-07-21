"""
    my d1 minis fail to reboot when something is connected to gnd. this uses pin D0 as a fake ground
    WARNING: esp8266 have max current 12mA on the gpio pins
"""

import machine

pin = machine.Pin(16, machine.Pin.OUT) # D0 on D1 mini
pin.value(0);
