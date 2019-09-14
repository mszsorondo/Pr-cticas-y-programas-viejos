#for i in [1,2,3,4,...]:
	#print ("Hola")
#el cuerpo del bucle se va a repetir tantas veces elementos haya dentro de la lista/tupla/diccionario/
#para ésto es necesario entender bien el verdadero funcionamiento del bucl. En éste caso no se esta imprimiendo el valor de la variable "k" tantas veces como elementos haya en la lista, sino que simplemente se imprimira "hola" tantas veces como se ejecute el bucle mas allá del valor de k.
#for j in ["asd", "asde", "asds"]:
	#print ("Charles")
	#en éste caso lo que pasará será que se imprimirá charles tres veces
 
 #imprimir elementos dentro de la estructura
#for n in ("Gabriel", "Joseph", "Tom", "Power Rangers"):
	#print(n)
#Lo que pasará será que se imprimirá cada elemento a cada vuelta de bucle (4)

#notaciones especiales con sentencia print
#for i in ("Tesla", "Bugatti", "Audi"):
#	print (i, end="#")
# En éste caso lo que pasará será que se imprimirá cada elemento en un solo renglón y lo que los separará será lo que esté entre comillas luego del end (en éste caso "#")



#STR
#for i in "Spacex":
	#print ("Hola")
#en éste caso los elementos de la cadena de texto son todas sus letras por lo tanto, se imprimira hola tantas veces como caracteres hayan en la cadena (6 en éste caso)

#email=False
#miEmail=input("Introduce tu direccion de email: ")
#for i in miEmail:
	#if "@" in (i):
	#OPCION2: if(i==@)
		#email=True
#if email==True:
	#print ("El email es correcto")
#else:
	#print ("El email es incorrecto")



#for i in "demand":
	#print ("hola", end=str(1))

#s=input()
#for i in s:
#	if "@" in s and "." in s:
#		i=True
#	else:
#		i=False

#if i is True:
#	print ("El email es correcto")
#else:
#	print ("El email es incorrecto")



#NOTACIONES ESPECIALES CON PRINT
#f"": sirve para concatenar el texto con el valor de la variable
#for i in range(4):#valor de i va de 0 a 4)
	#print(f"elemento número {i}")
#for i in range(4,10):#valor de i va de 4 a 10)
	#print(f"elemento número {i}")
#for i in range(4,11,2):#valor de i va de 4 a 11) Y DE DOS EN DOS
	#print(f"elemento número {i}")



#len()
#funcion len devuelve un valor numerico que equivale al numero de caracteres dentro de una cadena de texto, en este caso pedimos que se le asigne a i un rango de numeros que va a ser igual a la cantidad...
#...de elementos que se le den a email y luego le decimos que si arroba se encuentra dentro de la cadena de texto asignada a email convierta la variable valido en verdadera
#valido=False
#email=input()
#for i in range(len(email)):
	#if "@" in email:
		#valido=True

#if valido:
	#print ("Email correcto")
#else:
	#print ("Email mal escrito")