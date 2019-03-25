"""
Calcul de la somme d'une suite de nombre positifs ou nuls
"""

nombre,somme,grand_nombre = 0,0,0
x = int(input("Saisissez un nombre (0 pour quitter):"))

x += x
print (x)
nombre += 1	
print ("Nombre : ",nombre)
while x > 0:
	nombre += 1	
	
	
	x += x
	somme = x
	print ("Nombre : ",nombre)
	print ("Somme : ",somme)
	if somme > 100:
		grand_nombre +=1
	x = int(input("Saisissez un nombre (0 pour quitter):"))	
print ("Grand nombre : ",grand_nombre)
print (nombre, " saisie total dont  ", grand_nombre, " grands nombres > 100 !")

