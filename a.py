
from math import pi



texte = ("Calcul du volume d'un cône" )
print(len(texte)* "-" )
print (texte)
print(len(texte)* "_" )

h = float(input("Saisissez la hauteur (m) : "))
r = float(input("Saisissez le rayon (m) : "))
volCone = (pi * r**2 * h)/3.0


texte = ("Le volume du cône est de : " )

print(texte,round(volCone,2), "m3.")