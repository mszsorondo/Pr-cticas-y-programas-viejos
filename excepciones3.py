import math

def calcularaiz(num1):
	if num1<0:
		raise ValueError ("No se puede calcular la raíz cuadrada de un número negativo")
	else:
		return math.sqrt(num1)


try:
	print(calcularaiz(int(input("Introduce el número para calcular su raíz: "))))
except ValueError as ErrorRaiz:
	print ("No se puede introducir un número negativo")

print ("Programa terminado")