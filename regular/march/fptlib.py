from ftplib import FTP

def writeline(data):
	fd.write(data + "\n")

	f = FTP('ftp.test.rebex.net')
	f.login()
	f.cwd('/home/madisnit')
	fd = open('README', 'wt')
	f.retrlines('RETR README', writeline)
	fd.close()
	f.quit()
