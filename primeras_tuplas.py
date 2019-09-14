miTupla=("Carajo", "Mierda", True, 8)
#funciones para convertir en lista...
miLista=list(miTupla)
#print (miLista)
#print (miTupla)


#tambien se puede hacer lo contrario...
miLista2=["hola", 3, False]
miTupla2=tuple (miLista2)
#print (miTupla2)

#para saber si hay o no un elemento dentro de una tupla...
#print (3 in miTupla2)

#para saber cuantas veces aparece un elemento dentro de una tupla...
#print (miTupla2.count(False)) ##aparece una vez.

#para saber cuántos elementos hay dentro de una tupla...
#print (len(miTupla))


#ejemplo de TUPLA UNITARIA (tiene solo 1 elemento)...
#tutupla=("Carlos",)  #muy importante la coma al final porque si no la ponemos tomará cada caracter como un elemento
#print(len(tutupla))

#tutupla2=("Carlos")
#print (len(tutupla2)) #acá cada caracter es un elemento

#a la tupla escrita sin parentesis se la llama empaquetado de tuplaa la tupla escrita entre parentesis y con variables asignadas se la llama desempaquetado de tupla
#tuplanueva= ("Marco", 25, 4, 2000) 
#nombre, dia, mes, agno= tuplanueva   ##asignar variables a los elementos de una tupla
#print (nombre)
#print(dia)
#print(mes)
#print(agno)
