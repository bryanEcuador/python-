class prueba(object):
	def __init__(self):
		self.__privado = "valor privado"
		self.publico = "valor publico"

	def __metodoPrivado(self):
		return "soy privado"

	def metodoPublico(self):
		return "soy publico"

	def getPrivado(self):
		return self.__privado

	def setPrivado(self,valor)
		self.__privado = self.__metodoPrivado()

obj = prueba()