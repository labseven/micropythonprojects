import socket
import machine
import time
import writeToLCD

oled = writeToLCD.connectToDisplay()

def connectSocket(ip, port):
	s = socket.socket()
	addr_info = socket.getaddrinfo(ip, port)
	addr = addr_info[0][-1]
	s.connect(addr)
	# s.listen(1)

	return s
	print('connected to', addr)

def sendMessage(msg):
	s.sendall(msg)

print('running testSocket.py')

 # "labseven.space"
s = connectSocket("163.172.150.171", 1444)

pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

lastPinVal = pin.value();

messageQueue = []


while True:
	if(pin.value() != lastPinVal):
		lastPinVal = pin.value()
		if(pin.value()):
			print('button pressed')
			messageQueue.append(1)
			oled.fill(1)
			oled.show()
			time.sleep(.15)
			oled.fill(0)
			oled.text(' :D :D :D :D :D :D :D :D', 0, 0)
			oled.text('Button Pressed', 0, 12)
			oled.show()

		else:
			oled.fill(0)
			oled.show()

	else:
		oled.text('              .', 0, 0)
		oled.scroll(-1, 0)
		oled.show()


	if(len(messageQueue) > 0):
		sendMessage("Button Pressed")
		messageQueue.pop()


	# data = s.recv(128)
	# if(data):
	# 	print(str(data, 'utf8'))

	# print(pin.value())
	time.sleep(.01)
