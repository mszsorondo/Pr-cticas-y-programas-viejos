
def divide():
	try:
		op1=(float(input("Introduce el numerador: ")))
		op2=(float(input("Introduce el denominador: ")))
		print ("La división es: " + str(op1/op2))
		print ("Cálculo finalizado")
	except ValueError:
		print ("El valor introducido es erróneo")
	except ZeroDivisionError:
		print ("No se puede dividir entre cero")
divide()
