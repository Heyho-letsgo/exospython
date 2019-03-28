# coding: utf-8
class Personne: 
	# Définition de notre classe Personne
    """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""

    
    def __init__(self, nom,prenom,age,lieu): 
    	self.nom = nom
    	self.prenom = prenom
    	self.age = age
    	self.lieu = lieu

    def printfx (self):
    	print (self.nom, "pqsoidfmqsifdom")

p1 = Personne("Pierre","","","")

p1.printfx()

