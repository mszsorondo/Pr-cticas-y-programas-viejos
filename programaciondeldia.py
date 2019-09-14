#QUEREMOS HACER UN PROGRAMA QUE AL INSERTAR EL DÍA DE LA SEMANA IMPRIMA TODAS LAS COSAS 
#PENDIENTES A HACER Y QUE HAGA UNA SIMULACIÓN DE LO QUE SERÁ EL DÍA TENIENDO EN CUENTA LA MAYOR CANTIDAD DE VARIABLES POSIBLES
horas=15
dimensiones=["Biblia", "Fiuba","Salud","Marketing Digital","Python","VariablesMinimas"]
dia=input("Ingrese el día de la semana: ")
def DiagnósticoDiario():
	if dia=="Lunes" or "Jueves":
		dimensiones.pop(3)
		dimensiones.pop(3)
		return(dimensiones)
print (DiagnósticoDiario())

#def simulación():
#	if dia=="Lunes":


#class ingenieroPerf():
	#pass

#def fiuba(self, insertar, día):
#	ubicación="FIUBA Las Heras"
#	modalidad=insertar
#	d=día
#	if d==("Lunes" or "Jueves"):
#		up=6
#	elif d==("Martes" or "Miércoles" or "Viernes"):
#		up=7
#	elif d=="Sábado":
#		up=9


#class Bib():


