# las herencias se hacen con clase(clase heredada): los metodos constructores se heredan
#la herencia multiple se hace separando con , las clases padres
#pass es la palabra reservada para decir que no hay nada 
#toma el init de la primera clase padre declarada (primeraclasepadre,segundaclasepadre)

class humano:
	def __init__(self):
		print "soy un nuevo objeto"

pedro = humano()

raul = humano()

class hombre(humano):
	def __init__(self):
		print "soy un hombre"
	
pedro = hombre()