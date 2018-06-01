with open('test_db','rb') as binary_file:
	data = binary_file.read()
	print data
	binary_file.seek(0)
	couple_bytes = binary_file.read(2)
	print couple_bytes
