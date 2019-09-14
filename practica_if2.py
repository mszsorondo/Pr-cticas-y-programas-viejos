print ("Bienvenidos al Examen Físico de la Policía Federal Argentina")

num_dominadas=input("Introducir numero de dominadas realizadas: ")

def examen(repeticiones):
	estadofisico="El ingresante está apto físicamente"
	if repeticiones<=10:
		estadofisico="No alcanzó el mínimo de dominadas necesarias para ingresar"
	return estadofisico

print (examen(int(num_dominadas)))
