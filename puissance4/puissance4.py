#Fonctions
import fixpath
from random import randint
#Modeles
import modele
import modeleDehors
import modeleTop10
import modele5suite
import modeleDefi
import modeleN
#Affichages
import affichageMenu
import affichage
import affichage5suite
import affichageDefi


def puissance4():
	rejouer = True
	quitter = False
	rejoue = 0
	while rejouer :
		mode_de_jeu = affichageMenu.menu()
		if(mode_de_jeu == 0):
			rejouer = False
		if(mode_de_jeu == 1): #Jeu original
			modele.main()
		elif(mode_de_jeu == 2): #Mode VS IA
			modele.xaMain()
		elif(mode_de_jeu == 3): #Mode Dehors
			modeleDehors.dehorsMain()
		elif(mode_de_jeu == 4): #Mode Top10
			modeleTop10.top10Main()
		elif(mode_de_jeu == 5): #Mode 5alasuite
			modele5suite.cinqsuiteMain()
		elif(mode_de_jeu == 6): #Mode Defi +
			modeleDefi.defiMain()
		elif(mode_de_jeu == 7): #Mode n++ (Animation des pions)
			modeleN.nMain()
		valeurCorrecte = False
		if rejouer :
			while not valeurCorrecte:
				try:	
					rejoue = int(input("Voulez-vous rejouer ?  Tapez 1 pour rejouer ou 2 pour quitter : "))
					if(rejoue == 1 or rejoue == 2):
						valeurCorrecte = True
					else : 
						print("Entrez une des options proposées")
				except(ValueError) :
					print("Entrez un entier")    
		if(rejoue == 2 or rejoue == 0):
			rejouer = False
	print("")
	print("AU REVOIR, NOUS ESPÉRONS VOUS REVOIR BIENTÔT !".center(200))
	print("")		

if __name__ == "__main__":
   puissance4()

