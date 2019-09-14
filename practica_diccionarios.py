midiccionario={"Argentina":"Buenos Aires", "Chile":"Santiago", "Bolivia":"La Paz", "Uruguay":"Montevideo"}
#print (midiccionario["Bolivia"])
#print (midiccionario)



#podemos AGREGAR nuevos elementos a un diccionario de la siguiente manera...
#midiccionario["ITALIA"]="Lisboa"
#print (midiccionario)




#podemos MODIFICAR un elemento...
#midiccionario["ITALIA"]="ROMA"
#print (midiccionario)




#también podemos ELIMINAR un elemento...
#del midiccionario["Chile"]
#print (midiccionario)



#se puede RELACIONAR un diccionario con una tupla...
#mitupla= "Madrid", "París", "Berlín"
midiccionario2= {mitupla[0]:"España", mitupla[1]:"Francia", mitupla[2]:"Alemania"}


#print (midiccionario2)
#print (midiccionario2[mitupla[0]]) #es IGUAL que escribir la clave por medio de su valor en la tupla


#también podemos hacer una "clave:[lista]" siendo lista una serie de valores, podemos hacer lo mismo con tuplas e INCLUSIVE con otros diccionarios
#podemos hacer una "clave:{Diccionario}" ETC ETC

#LOS DICCIONARIOS POSEEN METODOS...
#print (midiccionario.keys())    #para mostrar solo las claves
#print (midiccionario.values())  #para mostrar solo los valores
#print (len(midiccionario))  #para mostrar la longitud en cantidad de elementos
