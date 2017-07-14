import socket
import machine
import time

def connectSocket(ip, port):
	s = socket.socket()
	addr_info = socket.getaddrinfo(ip, port)
	addr = addr_info[0][-1]
	s.connect(addr)
	return s
	print('connected to', addr)

print('running testSocket.py')

s = connectSocket("163.172.150.171", 1444)

pin = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
	print(pin.value())
	s.send('pin is at ' + str(pin.value()))
	time.sleep(.5)

