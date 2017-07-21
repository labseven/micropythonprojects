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
	s.send(msg)
	print('sent')

print('running futureboard')

 # "labseven.space"
# s = connect("192.168.34.91", 80)

pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
lastPinVal = pin.value();

messageQueue = []

def http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()

def http_post(url):
	_, _, host, path = url.split('/', 3)
	addr = socket.getaddrinfo(host, 80)[0][-1]
	s = socket.socket()
	s.connect(addr)
	s.send(bytes('POST /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
	while True:
		data = s.recv(100)
		if data:
			print(str(data, 'utf8'), end='')
		else:
			break
	s.close()


while True:
	if(pin.value() != lastPinVal):
		lastPinVal = pin.value()
		if(pin.value()):
			print('button pressed')
			messageQueue.append(1)



	if(len(messageQueue) > 0):
		# sendMessage(b'GET / HTTP/1.1\r\nHost: 192.168.34.91\r\n\r\n')

		http_post("http://192.168.34.91/upvote")
		messageQueue.pop()


	# data = s.recv(128)
	# if(data):
	# 	print(str(data, 'utf8'))

	# print(pin.value())
	time.sleep(.01)
