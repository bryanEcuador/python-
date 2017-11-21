#operaciones con archivos 

def escritura(dato_a,dato_b):
	prueba = open('prueba.txt','w')
	prueba.write(dato_a)
	prueba.write(dato_b)
	prueba.close
#escritura ('hola ','mundo')

def lectura():
	leer = open('prueba.txt','r')
	print(leer.read())
	leer.close
lectura()



