class Humano():
	def __init__(self):
		self.__altura=7

	def hablar(self):
		print (self.__altura)

	def gritar(self):
		return True

marco=Humano()
marco.__altura=5
marco.hablar()
print(marco.gritar())

