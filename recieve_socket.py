import socket
import machine
import time
import lcd

oled = lcd.connect()

def connect(ip, port):
	s = socket.socket()
	addr_info = socket.getaddrinfo(ip, port)
	addr = addr_info[0][-1]
	s.connect(addr)
	# s.listen(1)

	return s
	print('connected to', addr)

oled.fill(0)
oled.text("connecting...", 0, 0)
oled.show()

s = connect("163.172.150.171", 1444)
num_letters = 0
oled.fill(0)
oled.show()

while True:
    print(',')
    data = s.recv(128)
    if data:
        data_str = str(data, 'utf8')
        # print(str(data, 'utf8'))
        num_letters += 1;
        x = int((num_letters * 8) % 120)
        y = int((num_letters / 15)) * 10
        print(x, y)
        oled.text(data_str, x, y)
        oled.show()

    else:
        print('.', end='')

	time.sleep(.01)
