import socket
import machine
import time

def connect(ip, port):
	s = socket.socket()
	addr_info = socket.getaddrinfo(ip, port)
	addr = addr_info[0][-1]
	s.connect(addr)

	print('connected to', addr)
	return s

def sendMessage(msg):
	s.sendall(msg)

print('running futureboard')

 # "labseven.space"
s = connect("192.168.34.91", 80)

pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

lastPinVal = pin.value();

messageQueue = []


while True:
	if(pin.value() != lastPinVal):
		lastPinVal = pin.value()
		if(pin.value()):
			print('button pressed')
			messageQueue.append(1)



	if(len(messageQueue) > 0):
		sendMessage("Button: +1")
		messageQueue.pop()


	# data = s.recv(128)
	# if(data):
	# 	print(str(data, 'utf8'))

	# print(pin.value())
	time.sleep(.01)
