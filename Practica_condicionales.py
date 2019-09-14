
#CONCATENACIÓN DE OPERADORES DE COMPARACION...
#edad=-5

#if 0<edad<100:
	#print ("La edad es correcta")
#else:
	#print ("La edad es incorrecta")

#En éste caso lo que pasa es que evalúa si edad es mayor a 0, pero como no lo es ya directamente se salta la siguiente condicion (si edad<100) y ejecuta else.
#Si edad fuese mayor a 100 sí que evaluaría primero si edad es > a cero por una cuestion de orden.
#Si edad cumple con la condición IF, else se ignora directamente.

#/

#salario_presidente=(int(input("Introduce el salario del presidente: ")))
#print ("El salario del presidente es de: $",+salario_presidente)
#salario_director=(int(input("Introduce el salario del director: ")))
#print ("El salario del director es de: $",+salario_director)
#salario_jefe=(int(input("Introduce el salario del jefe: ")))
#print ("El salario del jefe es de: $",+salario_jefe)
#salario_admin=(int(input("Introduce el salario del administrativo: ")))
#print ("El salario del administrativo es de: $",+salario_admin)


#if salario_presidente>salario_director>salario_jefe>salario_admin:
	#print ("Todo esta en orden")

#else:
	#print ("Algo huele mal")









#OPERADORES LOGICOS AND Y OR:
#print ("Programa de becas para estudiantes año 2018")
#distancia=(int(input("Introduce distancia a la escuela: ")))
#hermanos=(int(input("Introduce la cantidad de hermanos:")))
#salario=(int(input("Introduce el salario familiar anual: ")))

#if distancia>40 and hermanos>2 or salario<=20000:
	#print ("El alumno tiene acceso al programa")

#else:
	#print ("No cumple los requisitos")





#OPERADOR IN:
#print ("Asignaturas electivas Ingeniería Informática: ")
#print ("Asignaturas disponibles en el programa: Python , Ruby , Java ")

#asignaturas=input("Asignatura: ")

#if "Python" in asignaturas:
	#print ("Has elegido cursar la asignatura Python")

#elif "Ruby" in asignaturas:
	#print ("Has elegido cursar la asignatura Ruby")

#elif "Java" in asignaturas:
	#print ("Has elegido cursar la asignatura Java")

#else:
	#print ("La asignatura no se encuentra en el programa")

#HECHO DE UNA MANERA MAS EFICIENTE Y CON MENOS CÓDIGO...

#print ("Bienvenido al programa de asignaturas electivas")
#print ("Escriba una asignatura electiva de las siguientes: Python , Ruby , Java ")

#asignatura=(input())
#opcion=asignatura.lower()

#if opcion in ("python", "ruby", "java"):
	#print ("Has elegido " +opcion)

#else:
	#print ("La asignatura elegida no está disponible")