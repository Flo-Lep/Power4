
import modele
import affichage
import affichage5suite

LARGEUR5suite = 9
HAUTEUR5suite = 6

def selectColumn5suite(plateau): #Permet au joueur de choisir une colonne
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
			print("Entrez un des numéros de colonnes proposés : ")
		if a:
			if (plateau[colonne][0] == -1 or plateau[colonne][1] == -1 or plateau[colonne][2] == -1 or plateau[colonne][3] == -1 or plateau[colonne][4] == -1 or plateau[colonne][5] == -1):
				b = True
			else : 
				print("Cette colonne est déjà remplie")
			if(a == True and b == True):
				ok = True
	return colonne

def winCheck5suite(plateau):
	#Colonne
	winner = -1
	for colonne in range(len(plateau)):
		for ligne in range(2):
			if(plateau[colonne][ligne] == plateau[colonne][ligne+1] == plateau[colonne][ligne+2] == plateau[colonne][ligne+3] == plateau[colonne][ligne+4] == 0):
				winner = 0
			if(plateau[colonne][ligne] == plateau[colonne][ligne+1] == plateau[colonne][ligne+2] == plateau[colonne][ligne+3] == plateau[colonne][ligne+4] == 1):
				winner = 1
	#Ligne
	for ligne in range(6):
		for colonne in range(3):
			if(plateau[colonne][ligne] == plateau[colonne+1][ligne] == plateau[colonne+2][ligne] == plateau[colonne+3][ligne] == plateau[colonne+4][ligne] == 0):
				winner = 0
			if(plateau[colonne][ligne] == plateau[colonne+1][ligne] == plateau[colonne+2][ligne] == plateau[colonne+3][ligne] == plateau[colonne+4][ligne] == 1):
				winner = 1
	#Diagonale(decroissantes-Coin sup gauche)
	for colonne in range(4):
		for ligne in range(2):
			if(plateau[colonne][ligne] == plateau[colonne+1][ligne+1] == plateau[colonne+2][ligne+2] == plateau[colonne+3][ligne+3] == plateau[colonne+4][ligne+4] == 0):
				winner = 0
			if(plateau[colonne][ligne] == plateau[colonne+1][ligne+1] == plateau[colonne+2][ligne+2] == plateau[colonne+3][ligne+3] == plateau[colonne+3][ligne+4] == 1):
				winner = 1
	#Diagonales(croissantes-Coin inf gauche)
	for colonne in range(4):
		for ligne in range(3):
			if (plateau[colonne][5-ligne] == plateau[colonne+1][4-ligne] == plateau[colonne+2][3-ligne] == plateau[colonne+3][2-ligne] == plateau[colonne+4][1-ligne] == 0):
				winner = 0
			if (plateau[colonne][5-ligne] == plateau[colonne+1][4-ligne] == plateau[colonne+2][3-ligne] == plateau[colonne+3][2-ligne] == plateau[colonne+4][1-ligne] == 1):
				winner = 1
	return winner

def assignPawn5suite(plateau, player_turn, colonne): #Assigne une case au pion en fonction de la col choisie
	if(plateau[colonne][5] == modele.VIDE):
		plateau[colonne][5] = player_turn
	elif(plateau[colonne][4] == modele.VIDE):
		plateau[colonne][4] = player_turn
	elif(plateau[colonne][3] == modele.VIDE):
		plateau[colonne][3] = player_turn
	elif(plateau[colonne][2] == modele.VIDE):
		plateau[colonne][2] = player_turn
	elif(plateau[colonne][1] == modele.VIDE):
		plateau[colonne][1] = player_turn
	elif(plateau[colonne][0] == modele.VIDE):
		plateau[colonne][0] = player_turn

def cinqsuiteMain(): #Fonction main du mode de Base
	plateau =[ [modele.VIDE for j in range(6)] for i in range(9) ]
	#JRJRJR(Gauche du plateau)
	for ligne in range(3):
		plateau[0][ligne*2] = modele.J2
	for ligne in range(3):
		plateau[0][2*ligne+1] = modele.J1
	#RJRJRJ(Droite du plateau)
	for ligne in range(3):
		plateau[8][ligne*2] = modele.J1
	for ligne in range(3):
		plateau[8][2*ligne+1] = modele.J2
	player_turn = 0
	win_Check = False
	end_Check = False
	while not end_Check and not win_Check :
		affichage.effacerEcran()
		affichage5suite.afficherRectangle5suite()
		affichage5suite.afficherCellule5suite(plateau)
		print("")
		print("C'est le tour du joueur",player_turn+1)
		print("")
		colonne = selectColumn5suite(plateau)
		assignPawn5suite(plateau, player_turn, colonne)
		affichage5suite.afficherCellule5suite(plateau)
		player_turn = (player_turn+1)%2
		end_Check = modele.endCheck(plateau, end_Check)
		winner = winCheck5suite(plateau)
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


