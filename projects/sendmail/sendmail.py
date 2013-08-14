import os

def quote(s) :
	return '"' + s.replace('"','\\"') + '"'
	
def shell(cmd) :
	print("Doing: \n\t" + cmd)
	os.system(cmd)

def sendmail(subject, to, msg) :
	shell('echo '+ quote(msg) +' | mail -s ' + quote(subject) + ' ' + quote(to))


sendmail('In reguard to the matter of "me"',
  "furiousgreencloud@gmail.com",
  "You didn't ask me before you took my favourite pencil")
