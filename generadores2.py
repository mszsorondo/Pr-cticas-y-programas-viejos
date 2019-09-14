def genCity(*ciudades):
	for elemento in ciudades:
			yield from elemento

ciudadesdevueltas=genCity("Buenos Aires", "Madrid", "Paris", "Berlín")


print (next(ciudadesdevueltas))

print (next(ciudadesdevueltas))

print (next(ciudadesdevueltas))

print (next(ciudadesdevueltas)) 

print (next(ciudadesdevueltas))

print (next(ciudadesdevueltas))

