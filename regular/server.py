import socket
s = socket.socket()
host = "192.168.2.198" 
port = 1234
s.bind((host,port))
s.listen(5)
while True:
	c, addr = s.accept()
	print 'Got connection from',addr
	c.send('thankyou for connecting\n')
	str1  = "nitesh"
	print len(str1)
	c.send(str1)
	c.close()
