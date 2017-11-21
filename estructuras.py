# if 
#print "cuantos libros lees anualmente"
#cantidad = int(input("/nEscribe la cantidad"))
#if cantidad >= 7:
#	print "eres un buen lector"
#else:
#	print "necesitas leer mas"

def alfa(numero):
     resultado = 0
     for j in range(1,5):
          resultado += numero +2
          print resultado
     final = beta(resultado)
     return final
def beta(numero):
     return numero/2.0
print(alfa(2))
