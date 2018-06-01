from urllib2 import urlopen
from xml.etree.ElementTree import XML

def get_data(url):
	d = urlopen(url)	
	dx = d.read()
	return dx
def print_usa(url):
	data = get_data(url)
	dy = XML(data)
		
	for cd in dy.findall("./CD"):
		if cd.find("./YEAR").text == "1988":
			print cd.find("./TITLE").text
if __name__=="__main__":
	print_usa("http://www.w3schools.com/js/cd_catalog.xml")
