import re
msg = "this is a my mobile number 979-1234-678 and my friend mobile numbers is 2345-3748-465 and my father mobile number is 876-3564-338 and my wife mobile number is 966-8833-407."
var = re.findall(r'\D(9(\d{3})-\d{4}-\d{3})',msg)
print var
