def seleccion(operacion):

	def suma(n,m):
		return n + m
	def multiplicacion(n,m):
		return n*m

	if operacion == "suma":
		return suma

	elif operacion == "multiplicacion":
		return multiplicacion

FGuardada = seleccion("suma")

print FGuardada(12,12)