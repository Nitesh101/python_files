import re
s = """I used to have 4563-987-1234 as my phone number,but now i have changed it to 567-345-2318.as it is numarically not 8585-454-4443 suitable with mylucky number i have changed it to 589-574-1258"""
match = re.findall(r'(\D\d{3}-\d{3}-\d{4})',s)
print match
