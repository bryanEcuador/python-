# es una funciion que recibe una funcion y devuelve una funcion
loggeado = True
usuario = "bryan"

def admin(f):
	def comprobar(*args,**kwargs): # para que sea un decorador globalizado con n atributos y argumentos
		if loggeado:
			f(*args,**kwargs) #la funcion que se va a ejecutar -> ejecuta la funcion 
		else:
			print "no tiene permiso para ejecutar", f.__name__
	return comprobar

def decorador(funcion):
	def funcionDecorada(*args,**kwargs):
		print "funcion ejecutada" , funcion.__name__
		funcion(*args,**kwargs)

	return funcionDecorada

@admin
@decorador # esto es igual a decorador(resta)(5,3)
def resta(n,m):
	print n-m

resta(3,5)

# decorando 
 
#

