import re
str = """ip address of john's machine is 125.258.143.698 and lucy's machine is 583.254.125.789.My machine's ip adress was 587.256.235.125 but recently it is changed to 125.254.148.159 and another valid ip is 125.254.123.200"""
match = re.findall(r'\d{3}.\d{3}.\d{3}.\d{3}',str)
op = []
for val in match:
	if all((int(x)<256 for x in val.split('.'))):
		op.append(val)
print(op)
