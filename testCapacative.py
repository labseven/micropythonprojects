import machine
import time

ADCpin = machine.ADC(0)

# pin = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
# ADCpin = adc.channel(1)


while True:
    print('pin is at ' + str(ADCpin.read()))
    time.sleep(.1)
