
ht = float(input("Entrez un prix hors taxe (0 pour quitter): "))


while ht != 0:
	ttc = (ht *20)/100
	print ("Prix ttc : ", ttc+ht)
	ht = float(input("Entrez un prix hors taxe (0 pour quitter): "))

print("Au revoir !")