while True:
    try:
    	n1=(int(input("Introduce el numerador: ")))
    	n2=(int(input("Introduce el denominador: ")))
    	break

    except ValueError:
    	print("Los valores introducidos no son correctos, inténtalo de nuevo")

def suma(num1, num2):
	try:
		return num1/num2
	except ZeroDivisionError:
		print ("No se puede dividir por cero")


print (suma(n1, n2))

print ("Se está ejecutando el resto del código, que puede ser muy importante")
