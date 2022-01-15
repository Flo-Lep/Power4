import modele
import affichage
import time

def assignPawnN(plateau, player_turn, colonne):
	if(plateau[colonne-1][5] == modele.VIDE):
		for ligne in range(6):
			plateau[colonne-1][ligne] = player_turn
			affichage.effacerEcran()
			affichage.afficherRectangle()
			affichage.afficherCellule(plateau)
			time.sleep(0.1)
			plateau[colonne-1][ligne] = modele.VIDE
		plateau[colonne-1][5] = player_turn
	elif(plateau[colonne-1][4] == modele.VIDE):
		for ligne in range(5):
			plateau[colonne-1][ligne] = player_turn
			affichage.effacerEcran()
			affichage.afficherRectangle()
			affichage.afficherCellule(plateau)
			time.sleep(0.1)
			plateau[colonne-1][ligne] = modele.VIDE
		plateau[colonne-1][4] = player_turn
	elif(plateau[colonne-1][3] == modele.VIDE):
		for ligne in range(4):
			plateau[colonne-1][ligne] = player_turn
			affichage.effacerEcran()
			affichage.afficherRectangle()
			affichage.afficherCellule(plateau)
			time.sleep(0.1)
			plateau[colonne-1][ligne] = modele.VIDE
		plateau[colonne-1][3] = player_turn
	elif(plateau[colonne-1][2] == modele.VIDE):
		for ligne in range(3):
			plateau[colonne-1][ligne] = player_turn
			affichage.effacerEcran()
			affichage.afficherRectangle()
			affichage.afficherCellule(plateau)
			time.sleep(0.1)
			plateau[colonne-1][ligne] = modele.VIDE
		plateau[colonne-1][2] = player_turn
	elif(plateau[colonne-1][1] == modele.VIDE):
		for ligne in range(2):
			plateau[colonne-1][ligne] = player_turn
			affichage.effacerEcran()
			affichage.afficherRectangle()
			affichage.afficherCellule(plateau)
			time.sleep(0.1)
			plateau[colonne-1][ligne] = modele.VIDE
		plateau[colonne-1][1] = player_turn
	elif(plateau[colonne-1][0] == modele.VIDE):
		plateau[colonne-1][0] = player_turn

def nMain():
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
		colonne = modele.selectColumn(plateau)
		assignPawnN(plateau, player_turn, colonne)
		affichage.afficherCellule(plateau)
		player_turn = (player_turn+1)%2
		end_Check = modele.endCheck(plateau, end_Check)
		winner = modele.winCheck(plateau)
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
