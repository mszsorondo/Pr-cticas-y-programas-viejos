class movil():
	def __init__(self, marca, modelo):
		
		self.marca=marca
		self.modelo=modelo
		self.marcha=False
		self.acelera=False
		self.frena=False
	def enmarcha(self):
		self.marcha=True
	def acelerar(self):
		self.acelera=True
	def frenar(self):
		self.frena=True
	
	def estado(self):
		print("Marca: ",self.marca, "\n Modelo: ", self.modelo, "\n Marcha: ", self.marcha, "\n Acelera: ", self.acelera, "\nFrena: ", self.frena)

class furgoneta(movil):
	def __init__(self, espacio, mark, model):
		super().__init__(mark, model)
		self.espacio=espacio
	def estado2(self):
		super().estado()
	def informarespaciodisp(self):
		print ("Hay ",self.espacio, "lugares restantes")
	def cargado(self, cargar):
		self.cargado=cargar
		if (cargar):
			return "La Furgoneta esta cargada"
		else:
			return "falta carga"


class moto(movil):
	def metwil(self):
		self.wilson=("Voy haciendo la Wilson y las demás subclases no pueden")
	def estado(self):
		print("Marca: ",self.marca, "\n Modelo: ", self.modelo, "\n Marcha: ", self.marcha, "\n Acelera: ", self.acelera, "\nFrena: ", self.frena, "\nCaballito: ", self.wilson)

Mimoto=moto("motomel", "dakar")
Mimoto.enmarcha()
Mimoto.acelerar()

Mimoto.metwil()
Mimoto.estado()
furgo1=furgoneta(7, "Volkswagen", "Multivan")
print(furgo1.cargado(True))
furgo1.estado2()
furgo1.informarespaciodisp()

class VEléctricos():
	def __init__(self):
		self.autonomía=100
	def cargando(self, cargar):
		self.carga=cargar
		if (cargar):
			return "El vehículo se está cargando"
		else:
			return "El vehículo está desenchufado"

class BiciEléctrica(movil, VEléctricos):
	pass


miBici=BiciEléctrica("Vairo", "Crossmountain")