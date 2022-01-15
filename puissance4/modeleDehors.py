
import modele
import affichage

def selectActionDehors(plateau, player_turn):#Propose au joueur d'ajouter ou d'éjecter un pion
	ok1 = False
	ok2 = False
	ajouter = False
	ejectionPossible = False
	valeurCorrecte = False
	while(not ok1 and not ok2):
		try :
			choix = int(input("Que souhaitez vous faire ? 1-Ajouter	2-Éjecter (pion de votre couleur) : "))
			if(choix >=1 and choix <=2):
				valeurCorrecte = True
			else :
				print("Choisissez parmi les valeurs proposées")
		except(ValueError):
			print("Entrez un entier proposé")
		if(valeurCorrecte and choix == 1):
			ajouter = True
		if(valeurCorrecte and choix == 2):
			if(plateau[0][5]== player_turn or plateau[1][5]== player_turn or plateau[2][5]== player_turn or plateau[3][5]== player_turn or plateau[4][5]== player_turn or plateau[5][5]== player_turn or plateau[6][5]== player_turn):
				ejectionPossible = True
			else:
				print("Vous ne pouvez pas éjecter de pion...")
		if(valeurCorrecte ==  True and ajouter == True):
			ok1 = True
		if(ejectionPossible == True and valeurCorrecte == True):
			ok2 = True
			
	return choix
				


def selectColumnEject(plateau, player_turn):#Selectionne la colonne pour l'éjection
	ok = False
	a = False
	b = False
	while not ok: #Ok = True --> a&b = True
		try:	
			colonne = int(input("Choisissez une colonne afin d'éjecter un pion : "))
			if(colonne > 0 and colonne < 8):
				a = True #La colonne appartient au plateau
			else :
				print("Cette colonne n'est pas disponible...")
		except(ValueError) :
			print("Entrez un des numéros de colonnes proposés : ")
		if a:
			if (plateau[colonne-1][5] == player_turn):
				b = True
			else : 
				print("Cette case est vide ou ce pion ne vous appartient pas")
			if(a == True and b == True):
				ok = True
	return colonne

def ejectPawn(colonne, plateau):#Éjecte un pion en fonction de la colonne (Fait redescendre les autres pions)
	plateau[colonne-1][5] = plateau[colonne-1][4]
	plateau[colonne-1][4] = plateau[colonne-1][3]
	plateau[colonne-1][3] = plateau[colonne-1][2]
	plateau[colonne-1][2] = plateau[colonne-1][1]
	plateau[colonne-1][1] = plateau[colonne-1][0]
	plateau[colonne-1][0] = modele.VIDE

def dehorsMain():
	plateau =[ [modele.VIDE for j in range(6)] for i in range(7) ]
	player_turn = 0
	win_Check = False
	end_Check = False
	while not end_Check and not win_Check :
		affichage.effacerEcran()
		affichage.afficherRectangle()
		affichage.afficherCellule(plateau)
		print("")
		print("C'est le tour du joueur",player_turn+1)
		print("")
		choix = selectActionDehors(plateau, player_turn)
		if(choix == 1): #On veut ajouter un pion
			colonne = modele.selectColumn(plateau)
			modele.assignPawn(plateau, player_turn, colonne)
		else:
			colonne = selectColumnEject(plateau, player_turn)
			ejectPawn(colonne, plateau)
		affichage.afficherCellule(plateau)
		player_turn = (player_turn+1)%2
		end_Check = modele.endCheck(plateau, end_Check)
		winner = modele.winCheck(plateau)
		if(winner == 0 or winner == 1):
			win_Check = True
	affichage.effacerEcran()
	affichage.afficherRectangle()
	affichage.afficherCellule(plateau)
	if(end_Check == True) :
		print("")
		print(" FIN DE LA PARTIE, ÉGALITÉ    ")
		print("")
	elif(winner == 0):
		print("")
		print(" FIN DE LA PARTIE, LE JOUEUR 1 A GAGNÉ !")
		print("")
	else :
		print("")
		print(" FIN DE LA PARTIE, LE JOUEUR 2 A GAGNÉ !")
		print("")


