import pwd
import os

def userexists(usuario):
	try:
		result = pwd.getpwnam(usuario)
	except:
		return 0
	return 1

def pathexists(directorio):
	if (directorio != ""):
		if (os.path.exists(directorio) == True):
			print("Existe")
			return 1
		else:
			print("No Existe")
			return 0
	print("No Existe")
	return 0