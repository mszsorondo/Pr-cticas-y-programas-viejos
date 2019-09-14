
class personaje():

	def __init__(self):
		self.__vida=400
		self.__mana=1500
		self.__energía=1000
		self.velocidad=0
		self.nombre=input("Introduce el nombre del personaje: ")
		self.velocidad=int(input("Introduce la velocidad en que camina el personaje: "))

	def caminar(self):
		
		



		if self.velocidad>0:

			chequeo=self.__chequeo()


		if (self.velocidad>0 and chequeo==True):
			print("Hola soy", self.nombre,"y estoy caminando")



		elif self.velocidad>0 and chequeo is not True:
			print ("Algo ha ido mal en el chequeo,", self.nombre , " no puede arrancar")

			self.velocidad=0



		else:
			print("Hola soy", self.nombre,"y estoy detenido")

	def printAtr(self):
		print(self.nombre, "tiene", self.__vida, " puntos de vida, su velocidad es de ", self.velocidad, "km/H, su energía es de ", self.__energía, "puntos, y su mana es de ", self.__mana, "puntos")



	def __chequeo(self):
		print("Realizando el chequeo interno")
		dinero="suficiente"
		arma=True
		ropa=True

		if (dinero=="suficiente" and arma==True and ropa==True):
			return True
		else:
			return False



Markitosz=personaje()
Markitosz.caminar()

print("A continuación creamos nuestro segundo objeto")

kaenna=personaje()

kaenna.caminar()

kaenna.printAtr()
Markitosz.printAtr()
kaenna.vida=5
#Nótese como a pesar de cambiar el valor de la variable vida dicha variable fue antes encapsulada dentro del método constructor mediante la escriturar del doble guión bajo.
#Sin embargo, sí se podrían modificar las demás variables almacenadas en el método inicial/initial/constructor ya que no `poseen el doble guión bajo.