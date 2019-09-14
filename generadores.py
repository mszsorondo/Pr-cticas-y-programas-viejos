def generapares(limite):
	num=1

	while num<limite:
		yield (num*2)
		num=num+1

variable=generapares(10)

print(next(variable))
#SUSPENCIÓN
print ("Aquí podría ir más código")

print(next(variable))
#SUSPENCIÓN
print ("Aquí podría ir más código")

print(next(variable))
#SUSPENCIÓN
print ("Aquí podría ir más código")

