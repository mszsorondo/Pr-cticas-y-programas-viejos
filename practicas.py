#quiero un programa que tenga una lista y que si encuentra la palabra "perro" que imprima dicha palabra.
#Ahora quiero que en vez de imprimir perro imprima la palabra invertida
cosas=["Buenos Aires", "aHola", "cuba", "venezuela", 5, True, "perro"]

for k in cosas:
	if k=="aHola":
		print (k[::-1])