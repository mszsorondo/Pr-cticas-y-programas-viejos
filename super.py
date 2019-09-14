class Estudiante():
	def __init__(self, nombre, apellido, residencia):
		self.nombre=nombre
		self.apellido=apellido
		self.lugarderesidencia=residencia
	def descripcion(self):
		print ("Nombre: ", self.nombre, "Apellido: ", self.apellido, "Residencia: ", self.lugarderesidencia)
class EstudianteDeIngeniería(Estudiante):
	def __init__(self, calif_Analisis, calif_Quim, calif_IPC, calif_ICSE, name, surname, resid):
		super().__init__(name, surname, resid)
		self.analisis=calif_Analisis
		self.quimica=calif_Quim
		self.ipc=calif_IPC
		self.icse=calif_ICSE
	def calificaciones(self):
		print ("Calificaciones:  ", "Análisis matemático: ", self.analisis, "Química: ",
		self.quimica, "Introducción al Pensamiento Científico: ", self.ipc, "Introducción al Conocimiento de la Sociedad y el Estado: ", self.icse)
	def descripcion(self):
		super().descripcion()
	

Marco=EstudianteDeIngeniería("Desconocido", 5, 9, 7, "Marco", "Sánchez Sorondo", "Ciudad de Buenos Aires")
Marco.calificaciones()
Marco.descripcion()
#Qué es lo que pasa, que los estudiantes de ingeniería también son estudiantes en general que tienen nombre apellido y residencia. El método inicial de la superclase esta sobreescrito por el de la subclase. 
#Es por eso que vamos a acceder a la función "super().__init__()" para que también tenga los parámetros del método constructor padre. 
print(isinstance(Marco, EstudianteDeIngeniería)) #Esta funcion isinstance sirve para saber si un determinado objeto pertenece a una determinada clase o subclase. Ser Estudiante de Ingeniería implica ser Estudiante.