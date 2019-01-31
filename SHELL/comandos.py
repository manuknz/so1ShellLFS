import os
import pwd
import grp
import subprocess
import shutil

#Funcion para mover
def mover(parametros):
	sinEsp = parametros.split(" ")
	if (len(sinEsp) == 2):
		viejo = sinEsp[0]
		nuevo = sinEsp[1]
		if (pathexists(viejo) == 1):
			if (pathexists(nuevo) == 1):
				shutil.move(viejo, nuevo)
				
		else:
			print("No existe!")
	else:
		print("Parametros incorrectos!")
		return	

#Funcion para renombrar
def rename(parametros):
	sinEsp = parametros.split(" ")
	if (len(sinEsp) == 2):
		viejo = sinEsp[0]
		nuevo = sinEsp[1]
		if (pathexists(viejo) == 1):
			os.renames(viejo, nuevo)
			print("Se renombro con exito!")
		else:
			print("No existe!")
	else:
		print("Parametros incorrectos!")
		return

#Funcion para listar directorios
def ld(directorio):
	sinEsp = directorio.split(" ")
	directorio2 = sinEsp[0]
	if (len(sinEsp) == 1):
		if (pathexists(directorio2)):
			for path, dirs, files in os.walk(directorio):
				if (path == directorio):
					for direc in dirs:
						print(direc)
					for archi in files:
						print(archi)
					break
		else:
			print("La ruta no existe!")
			return
	else:
		print("Parametros incorrectos!")
		return

#Funcion para crear directorios
def dirmk(directorio):
	sinEsp = directorio.split(" ")
	if (len(sinEsp) == 1):
		sinBar = directorio.split("/")
		if (len(sinBar) < 2):
			print("Debe empezar con /, ruta incorrecta!")
			return
		sinBar.remove("")
		directorio2 = "/"
		for i in range(len(sinBar) - 1):
			if (i == 0):
				directorio2 = directorio2 + sinBar[i]
			else:
				directorio2 = directorio2 + "/" + sinBar[i]
			if (os.path.isdir(directorio2) == False):
				print("La ruta " + directorio2 + " no existe!")
				return
		if (os.path.isdir(directorio2 + "/" + sinBar[len(sinBar) - 1]) == True):
				print("La ruta ya existe!")
				return
		os.mkdir(directorio)
		print("La ruta se creo!")
	else:
		print("Parametros incorrectos!")
		return

#Funcion para cambiar el modo de lectura/escritura
def modch(parametros):
	sinEsp = parametros.split(" ")
	if (len(sinEsp) == 2):
		directorio = sinEsp[0]
		modo = sinEsp[1]
		try:
			modOctal = int(modo, 8)
		except:
			print("Numero incorrecto!")
			return
		if (pathexists(directorio) == 1):
			if(0o0 <= modOctal <= 0o777):
				os.chmod(directorio, modOctal)
				print("Se cambio correctamente!")
				if(os.path.isdir(directorio)):
					listArchivos = os.listdir(directorio)
					for actual in listArchivos:
						modch((directorio + "/" + actual) + " " + modo)
			else:
				print("Modo/numero incorrecto!")
				return
		else:
			print("La ruta no existe!")
			return		
	else:
		print("Parametros incorrectos!")
		return

#Funcion para cambiar el propietario
def ownch(parametros):
	sinEsp = parametros.split(" ")
	if (len(sinEsp) == 3):
		directorio = sinEsp[0]
		duenho = sinEsp[1]
		grupo = sinEsp[2]
		if (userexists(duenho) == 1):
			if (pathexists(directorio) == 1):
				if (groupexists(grupo) == 1):
					result = pwd.getpwnam(duenho)
					result2 = grp.getgrnam(grupo)
					IDduenho = result[2]
					IDgrupo = result2[2]
					os.chown(directorio, IDduenho, IDgrupo)
					print("Se cambio de propietario!")
					if(os.path.isdir(directorio)):
						listArchivos = os.listdir(directorio)
						for actual in listArchivos:
							ownch((directorio + "/" + actual) + " " + duenho + " " + grupo)
				else:
					print("El grupo no existe!")
					return
			else:
				print("La ruta no existe!")
				return
		else:
			print("El usuario " + duenho + " no existe!")
			return
	else:
		print("Parametros incorrectos!")
		return

def passch(parametros):
	sinEsp = parametros.split(" ")
	if (len(sinEsp) == 1):
		usuario = sinEsp[0]
		if (userexists(usuario) == 1):
			os.system("passwd " + usuario)
		else:
			print("El usuario no existe!")
	else:
		print("Parametros incorrectos!")
		return

def adduser(parametros):
	sinEsp = parametros.split(" ")
	if (len(sinEsp) < 1):
		print("Parametros incorrectos!")
		return
	elif(len(sinEsp) == 3):
			usuario = sinEsp[0]
			horario = sinEsp[1]
			lugarConexion = sinEsp [2]
			if ((userexists(usuario)) == 0):
				os.system("useradd " + usuario + " -c " + "'" + "Horas de trabajo " + str(horario) + " - Lugar de conexion " + str(lugarConexion) + "'")
				print("Se creo el usuario!")
			else:
				print("El usuario ya existe!")
				return
	else:
		print("Parametros incorrectos!")
		return

def userexists(usuario):
	try:
		result = pwd.getpwnam(usuario)
	except:
		return 0
	return 1

def pathexists(directorio):
	if (directorio != ""):
		if (os.path.exists(directorio) == True):
			return 1
	return 0

def groupexists(grupo):
	try:
		result = grp.getgrnam(grupo)
	except:
		return 0
	return 1

def otrashell(comando):
	try:
		subprocess.run(comando)
	except:
		print("Comando no reconocido!")