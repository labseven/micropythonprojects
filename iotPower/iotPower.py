import socket
import machine
import time



relayPins = [16]
relayStatus = [0] * len(relayPins)
relays = []

buttonPins = []
buttonStatus = [0] * len(buttonPins)
buttons = []

def connect(host, port):
	s = socket.socket()
	addr_info = socket.getaddrinfo(host, port)
	addr = addr_info[0][-1]
	s.connect(addr)

	print('connected to', addr)
	return s

def recieve(s):
    data_str = ""
    while True:
        print('recieving')
        print(data_str)
        data = s.recv(128)
        if data:
            data_str += str(data, 'utf8')
            # print(str(data, 'utf8'))
        else:
            break
    print('transmision over')
    return data_str


# Setup pins
for relayPin in relayPins:
    relays.append(machine.Pin(relayPin, machine.Pin.OUT))

for buttonPin in buttonPins:
    buttons.append(machine.Pin(buttonPin, machine.Pin.IN))


s = connect('labseven.space', 4444)

print(relays)

while True:
    msg = recieve(s)
    print(msg)
    if(msg == '1'):
        relays[0].value(0)
    else:
        relays[0].value(1)

    print('.', end='')

    time.sleep(.01)
