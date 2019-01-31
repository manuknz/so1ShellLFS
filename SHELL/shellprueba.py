from cmd import Cmd
import comandos

class LFShell(Cmd):
	prompt = 'so1> '

	def emptyline(self):
		pass

	def default(self, inp):
		comandos.otrashell(inp)

	def do_salir(self, inp):
		print("Nos vimos")
		return True

	def do_add(self, inp):
		print("Agregando '{}'".format(inp))

	def do_rename(self, inp):
		comandos.rename(inp)

	def do_ld(self, inp):
		comandos.ld(inp)

	def do_dirmk(self, inp):
		comandos.dirmk(inp)

	def do_modch(self, inp):
		comandos.modch(inp)

	def do_ownch(self, inp):
		comandos.ownch(inp)

	def do_passch(self, inp):
		comandos.passch(inp)

	def do_adduser(self, inp):
		comandos.adduser(inp)

	def help_dirmk(self):
		print("Crea un directorio nuevo a partir de la ruta dada")

LFShell().cmdloop()