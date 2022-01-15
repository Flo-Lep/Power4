from random import randint
import affichage

VIDE = -1
J1 = 0 #Jaune
J2 = 1 #Rouge
LARGEUR = 7
HAUTEUR = 6

def selectColumn(plateau): #Permet au joueur de choisir une colonne
	ok = False
	a = False
	b = False
	while not ok: #Ok = True --> a&b = True
		try:	
			colonne = int(input("Choisissez une colonne : "))
			if(colonne > 0 and colonne < 8):
				a = True #La colonne appartient au plateau
			else :
				print("Cette colonne n'est pas disponible...")
		except(ValueError) :
			print("Entrez un des numéros de colonnes proposés... ")
		if a:
			if (plateau[colonne-1][0] == -1 or plateau[colonne-1][1] == -1 or plateau[colonne-1][2] == -1 or plateau[colonne-1][3] == -1 or plateau[colonne-1][4] == -1 or plateau[colonne-1][5] == -1):
				b = True
			else : 
				print("Cette colonne est déjà remplie")
			if(a == True and b == True):
				ok = True
	return colonne


def assignPawn(plateau, player_turn, colonne): #Assigne une case au pion en fonction de la col choisie
	if(plateau[colonne-1][5] == VIDE):
		plateau[colonne-1][5] = player_turn
	elif(plateau[colonne-1][4] == VIDE):
		plateau[colonne-1][4] = player_turn
	elif(plateau[colonne-1][3] == VIDE):
		plateau[colonne-1][3] = player_turn
	elif(plateau[colonne-1][2] == VIDE):
		plateau[colonne-1][2] = player_turn
	elif(plateau[colonne-1][1] == VIDE):
		plateau[colonne-1][1] = player_turn
	elif(plateau[colonne-1][0] == VIDE):
		plateau[colonne-1][0] = player_turn


def endCheck(plateau, end_Check): #Regarde si le plateau est rempli
	cases_remplies = 0
	for ligne in range(len(plateau)):
 		for colonne in range(len(plateau[ligne])):
 			if(plateau[ligne][colonne]!=-1):
 				cases_remplies = cases_remplies + 1
 			if (cases_remplies == len(plateau)*6): #nbr de cases totales du plateau
 				end_Check = True
	return end_Check


def winCheck(plateau): #Regarde si 4 pions sont alignés
	#Colonne
	winner = -1
	for colonne in range(len(plateau)):
		for ligne in range(3):
			if(plateau[colonne][ligne] == plateau[colonne][ligne+1] == plateau[colonne][ligne+2] == plateau[colonne][ligne+3] == 0):
				winner = 0
			if(plateau[colonne][ligne] == plateau[colonne][ligne+1] == plateau[colonne][ligne+2] == plateau[colonne][ligne+3] == 1):
				winner = 1
	#Ligne
	for ligne in range(6):
		for colonne in range(4):
			if(plateau[colonne][ligne] == plateau[colonne+1][ligne] == plateau[colonne+2][ligne] == plateau[colonne+3][ligne] == 0):
				winner = 0
			if(plateau[colonne][ligne] == plateau[colonne+1][ligne] == plateau[colonne+2][ligne] == plateau[colonne+3][ligne] == 1):
				winner = 1
	#Diagonale(decroissantes-Coin sup gauche)
	for colonne in range(4):
		for ligne in range(3):
			if (plateau[colonne][ligne] == plateau[colonne+1][ligne+1] == plateau[colonne+2][ligne+2] == plateau[colonne+3][ligne+3] == 0):
				winner = 0
			if(plateau[colonne][ligne] == plateau[colonne+1][ligne+1] == plateau[colonne+2][ligne+2] == plateau[colonne+3][ligne+3] == 1):
				winner = 1
	#Diagonales(croissantes-Coin inf gauche)
	for colonne in range(4):
		for ligne in range(3):
			if (plateau[colonne][5-ligne] == plateau[colonne+1][4-ligne] == plateau[colonne+2][3-ligne] == plateau[colonne+3][2-ligne] == 0):
				winner = 0
			if (plateau[colonne][5-ligne] == plateau[colonne+1][4-ligne] == plateau[colonne+2][3-ligne] == plateau[colonne+3][2-ligne] == 1):
				winner = 1
	return winner
	


def main(): #Fonction main du mode de Base
	plateau =[ [VIDE for j in range(6)] for i in range(7) ]
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
		colonne = selectColumn(plateau)
		assignPawn(plateau, player_turn, colonne)
		affichage.afficherCellule(plateau)
		player_turn = (player_turn+1)%2
		end_Check = endCheck(plateau, end_Check)
		winner = winCheck(plateau)
		if(winner == 0 or winner == 1):
			win_Check = True
	if(end_Check == True) :
		print("")
		print(" FIN DE LA PARTIE, ÉGALITÉ    ")
		print("")
	elif(winner == 0):
		print("")
		print(" FIN DE LA PARTIE, LE JOUEUR 1 A GAGNÉ")
		print("")
	else :
		print("")
		print(" FIN DE LA PARTIE, LE JOUEUR 2 A GAGNÉ")
		print("")


def xaMain(): #Fonction main du mode contre l'IA
	plateau =[ [VIDE for j in range(6)] for i in range(7) ]
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
		colonne = selectColumn(plateau)
		assignPawn(plateau, player_turn, colonne)
		affichage.afficherCellule(plateau)
		colonne = randint(1,7)
		assignPawn(plateau, player_turn+1, colonne)
		affichage.afficherCellule(plateau)
		end_Check = endCheck(plateau, end_Check)
		winner = winCheck(plateau)
		if(winner == 0 or winner == 1):
			win_Check = True
	if(end_Check == True) :
		print("")
		print(" FIN DE LA PARTIE, ÉGALITÉ    ")
		print("")
	elif(winner == 0):
		print("")
		print(" FIN DE LA PARTIE, LE JOUEUR 1 A GAGNÉ")
		print("")
	else :
		print("")
		print(" FIN DE LA PARTIE, LE JOUEUR 2 A GAGNÉ")
		print("")



