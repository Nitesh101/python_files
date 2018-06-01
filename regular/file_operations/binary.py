output_file = open('myfile.bin','wb')
output_file.write(b'\x0a\x1b\x2c')
output_file.write(b'\x3d\x4e\x5f')
output_file.close()
