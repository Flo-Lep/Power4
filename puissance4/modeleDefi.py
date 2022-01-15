
import modele
import modeleDehors
import affichage
import affichageDefi

ENCLUME = 2
MUR = 3
X2 = 4
BRISEUR = 5

def selectActionDefi(): #Propose au joueur d'Ajouter un pion ou d'utiliser un pion Power
	a = False
	b = False
	while not a and not b :
		try :
			choix = int(input("Que souhaitez vous faire ? 1-Ajouter un pion 2-Utiliser un pion Power : "))
			if(choix == 1):
				a = True
			elif(choix == 2):
				b = True
			else:
				print("Entrez une des valeurs proposées")
		except(ValueError):
			print("Entrez un entier")
	return choix

def selectPowerPawn(powerJ1,powerJ2,player_turn): #Permet au joueur de sélectionner un pion power
	enclume = False
	mur = False
	x2 = False
	briseur = False
	while not enclume and not mur and not x2 and not briseur :
		try :
			power = int(input("Veuillez selectionner un pion Power 1-Enclume  2-Mur  3-x2  4-Briseur : "))
			if(player_turn == 0): #Tour du joueur 1
				if(power == 1):
					if(1 in powerJ1):
						enclume = True
					else:
						print("Vous avez déjà joué ce pion Power")
				elif(power == 2):
					if(2 in powerJ1):
						mur = True
					else:
						print("Vous avez déjà joué ce pion Power")
				elif(power == 3):
					if(3 in powerJ1):
						x2 = True
					else:
						print("Vous avez déjà joué ce pion Power")	
				elif(power == 4):
					if(4 in powerJ1):
						briseur = True
					else:
						print("Vous avez déjà joué ce pion Power")
				else:
					print("Entrez une des valeurs proposées")
			else: #Tour du Joueur 2
				if(power == 1):
					if(1 in powerJ2):
						enclume = True
					else:
						print("Vous avez déjà joué ce pion Power")
				elif(power == 2):
					if(2 in powerJ2):
						mur = True
					else:
						print("Vous avez déjà joué ce pion Power")
				elif(power == 3):
					if(3 in powerJ2):
						x2 = True
					else:
						print("Vous avez déjà joué ce pion Power")	
				elif(power == 4):
					if(4 in powerJ2):
						briseur = True
					else:
						print("Vous avez déjà joué ce pion Power")
				else:
					print("Entrez une des valeurs proposées")
		except(ValueError):
			print("Entrez l'entier correspondant au pion power souhaité ")
	return power

def enclumePawn(plateau, colonne): #Place le pion ENCLUME
	for i in range(6):
		plateau[colonne-1][i] = modele.VIDE
	plateau[colonne-1][5] = ENCLUME

def murPawn(plateau, colonne): #Place le pion MUR
	if(plateau[colonne-1][5] == modele.VIDE):
		plateau[colonne-1][5] = MUR
	elif(plateau[colonne-1][4] == modele.VIDE):
		plateau[colonne-1][4] = MUR
	elif(plateau[colonne-1][3] == modele.VIDE):
		plateau[colonne-1][3] = MUR
	elif(plateau[colonne-1][2] == modele.VIDE):
		plateau[colonne-1][2] = MUR
	elif(plateau[colonne-1][1] == modele.VIDE):
		plateau[colonne-1][1] = MUR
	elif(plateau[colonne-1][0] == modele.VIDE):
		plateau[colonne-1][0] = MUR

def x2Pawn(plateau, colonne): #Place le pion X2
	if(plateau[colonne-1][5] == modele.VIDE):
		plateau[colonne-1][5] = X2
	elif(plateau[colonne-1][4] == modele.VIDE):
		plateau[colonne-1][4] = X2
	elif(plateau[colonne-1][3] == modele.VIDE):
		plateau[colonne-1][3] = X2
	elif(plateau[colonne-1][2] == modele.VIDE):
		plateau[colonne-1][2] = X2
	elif(plateau[colonne-1][1] == modele.VIDE):
		plateau[colonne-1][1] = X2
	elif(plateau[colonne-1][0] == modele.VIDE):
		plateau[colonne-1][0] = X2

def briseurPawn(plateau, colonne): #Place le pion BRISEUR
	if(plateau[colonne-1][5] == modele.VIDE):
		plateau[colonne-1][5] = BRISEUR
	elif(plateau[colonne-1][4] == modele.VIDE):
		plateau[colonne-1][4] = BRISEUR
	elif(plateau[colonne-1][3] == modele.VIDE):
		plateau[colonne-1][3] = BRISEUR
	elif(plateau[colonne-1][2] == modele.VIDE):
		plateau[colonne-1][2] = BRISEUR
	elif(plateau[colonne-1][1] == modele.VIDE):
		plateau[colonne-1][1] = BRISEUR
	elif(plateau[colonne-1][0] == modele.VIDE):
		plateau[colonne-1][0] = BRISEUR

def selectColumnEjectBriseur(plateau, player_turn):#Selectionne la colonne pour l'éjection (Fonction du BRISEUR)
	a = False
	b = False
	while not a and not b:
		try :
			colonne = int(input(" Choisissez une colonne afin d'éjecter un pion (Capacité Briseur) : "))
			if(colonne > 0 and colonne < 8):
				a = True #La colonne appartient au plateau
			else :
				print(" Cette colonne n'est pas disponible...")
		except(ValueError) :
			print(" Entrez un des numéros de colonnes proposés : ")
		if a :
			if(plateau[colonne-1][5] == player_turn+1): #Si c'est un pion adverse
				b = True
			else :
				print("Vous ne pouvez pas éjecter votre propre pion, éjectez un pion adverse ")
	return colonne


def defiMain():
	plateau =[ [modele.VIDE for j in range(6)] for i in range(7) ]
	player_turn = 0
	win_Check = False
	end_Check = False
	powerJ1 = [1,2,3,4] #Permettent de vérifier que le joueur n'a pas déjà joué le pion
	powerJ2 = [1,2,3,4]
	while not end_Check and not win_Check :
		affichage.effacerEcran()
		affichage.afficherRectangle()
		affichageDefi.afficherCelluleDefi(plateau)
		print("")
		print("C'est le tour du joueur",player_turn+1)
		print("")
		choix = selectActionDefi()
		if(choix == 1): #On veut ajouter un pion
			colonne = modele.selectColumn(plateau)
			modele.assignPawn(plateau, player_turn, colonne)
		else : #Choix == 2
			power = selectPowerPawn(powerJ1,powerJ2,player_turn)
			if(power == 1): #Enclume
				if(player_turn == 0):
					powerJ1.remove(power) #On retire le pion pour ne pas qu'il soit joué 2 fois
				else :
					powerJ2.remove(power)
				colonne = modele.selectColumn(plateau)
				enclumePawn(plateau, colonne)
				affichageDefi.afficherCelluleDefi(plateau)
			elif(power == 2): #Mur
				if(player_turn == 0):
					powerJ1.remove(power)
				else :
					powerJ2.remove(power)
				colonne = modele.selectColumn(plateau)
				murPawn(plateau, colonne)
				affichage.effacerEcran()
				affichage.afficherRectangle()
				affichageDefi.afficherCelluleDefi(plateau)
				print("Le mur vous permet de jouer un pion normal à la suite")
				print("")
				colonne = modele.selectColumn(plateau)
				modele.assignPawn(plateau, colonne, player_turn)#Soucis avec le 2eme pion...Pq???
			elif(power == 3): #x2
				if(player_turn == 0):
					powerJ1.remove(power)
				else :
					powerJ2.remove(power)
				colonne = modele.selectColumn(plateau)
				x2Pawn(plateau, colonne)
				affichage.effacerEcran()
				affichage.afficherRectangle()
				affichageDefi.afficherCelluleDefi(plateau)
				print("Le X2 vous permet de jouer un pion normal à la suite")#Soucis avec le deuxieme pion...Pq???
				colonne = modele.selectColumn(plateau)
				modele.assignPawn(plateau, colonne, player_turn)
			elif(power == 4): #Briseur
				if(player_turn == 0):
					powerJ1.remove(power)
				else :
					powerJ2.remove(power)
				colonne = modele.selectColumn(plateau)
				briseurPawn(plateau, colonne)
				affichage.effacerEcran()
				affichage.afficherRectangle()
				affichageDefi.afficherCelluleDefi(plateau)
				colonne = selectColumnEjectBriseur(plateau, player_turn)
				modeleDehors.ejectPawn(colonne, plateau)
		affichage.effacerEcran()
		affichage.afficherRectangle()
		affichageDefi.afficherCelluleDefi(plateau)
		player_turn = (player_turn+1)%2
		end_Check = modele.endCheck(plateau, end_Check)
		winner = modele.winCheck(plateau)
		if(winner == 0 or winner == 1):
			win_Check = True
	if(end_Check == True) :
		print("")
		print("FIN DE LA PARTIE, ÉGALITÉ")
		print("")
	elif(winner == 0):
		print("FIN DE LA PARTIE, LE JOUEUR 1 A GAGNÉ")
	else :
		print("FIN DE LA PARTIE, LE JOUEUR 2 A GAGNÉ")
 
