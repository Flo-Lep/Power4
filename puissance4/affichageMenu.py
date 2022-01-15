import affichage

def menu():
	affichage.effacerEcran()
	print("")
	print("")
	print("================".center(200))
	print("Puissance4".center(200))
	print("================".center(200))
	print("")
	print("")
	print("1: Jouer".center(200))
	print("")
	print("2: Quitter".center(200))
	print("")
	print("")
	print("")
	valeurCorrecte = False
	choix = 0
	while not valeurCorrecte :
		try :
			print("Que voulez-vous faire ? : ".center(200))
			valeur = int(input("".center(100)))
			if(valeur >= 1 and valeur <= 2):
				valeurCorrecte = True
			else :
				print("Option incorrecte, choisissez parmi ceux proposés".center(200))
		except(ValueError):
			print("Entrez un en entier".center(200))
	if(valeur == 1):
		affichage.effacerEcran()
		print("")
		print("")
		print("=================".center(200))
		print("MODE DE JEU".center(200))
		print("=================".center(200))
		print("")
		print("")
		print("1- ORIGINAL".center(200))
		print("")
		print("")
		print("")
		print("2- Xa".center(200))
		print("")
		print("")
		print("")
		print("3- DEHORS".center(200))
		print("")
		print("")
		print("")
		print("4- TOP10".center(200))
		print("")
		print("")
		print("")
		print("5- 5 À LA SUITE".center(200))
		print("")
		print("")
		print("")
		print("6- DÉFI +".center(200))
		print("")
		print("")
		print("")
		print("7- n++".center(200))
		print("")
		print("")
		print("")
		valeurCorrecte = False
		while not valeurCorrecte :
			try :
				print("Choisissez un mode de jeu : ".center(200))
				valeur = int(input("".center(100)))
				if(valeur >= 1 and valeur <= 7):
					valeurCorrecte = True
					choix = valeur
				else :
					print("Mode de jeu incorrect, choisissez parmi ceux proposés".center(200))
			except(ValueError):
				print("Entrez un entier...".center(200))
	return choix


