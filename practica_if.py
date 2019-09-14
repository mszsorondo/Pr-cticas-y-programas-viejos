
#en la primera línea de código le ordenamos al programa que imprima un mensaje en pantalla...
print ("Bienvenidos al programa de evaluación de alumnos")

#en la segunda línea declaramos la variable nota_alumno y la igualamos a la funcion predeterminada de python "input()"
#la función predeterminada input ordena que hasta que no se le asigne un dato a la variable, el programa no continúa, PERO...
#...la función predeterminada input solo acepta valores de tipo "string" (cadena de TEXTO), por lo tanto si al ejecutar el programa le decimos a la consola que nota_alumno=7...
#...7 va a ser considerado como un dato de texto...

nota_alumno=input("Introduzca la nota del alumno: ")

def evaluacion(nota):
	valoracion="Aprobado"
	if nota<6:
		valoracion="Desaprobado"
	return valoracion


#... ES POR ELLO que vamos a hacer que el valor de nota_alumno=input(str) se CONVIERTA en un valor INT (entero)
print (evaluacion(int(nota_alumno)))