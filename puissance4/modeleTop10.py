
import modele
import affichage
import modeleDehors

def selectColumnTop10(plateau, x): #Permet au joueur de remettre son pion
	ok = False
	a = False
	b = False
	while not ok: #Ok = True --> a&b = True
		try:	
			colonne = int(input("Votre pion n'appartenait pas à une rangée de 4, remettez-le dans une colonne différente : "))
			if(colonne > 0 and colonne < 8):
				a = True #La colonne appartient au plateau
			else :
				print("Cette colonne n'est pas disponible...")
		except(ValueError) :
			print("Entrez un des numéros de colonnes proposés... ")
		if a:
			if (x!=colonne):
				b = True
			else : 
				print("Vous ne pouvez pas remettre un pion dans la colonne dont vous venez d'éjecter un pion (sauf si vous n'avez pas le choix)") #J'espère que vous aurez toujours le choix (voir règles du jeu)
			if(a == True and b == True):
				ok = True
	return colonne


def winCheckTop10(plateau, colonne, player_turn): #Renvoie la valeur du joueur si 4 pions sont alignés
	#Colonne
	winner = -1
	if(plateau[colonne-1][5] == plateau[colonne-1][4] == plateau[colonne-1][3] == plateau[colonne-1][2] == player_turn):
		winner = player_turn
	#Lignes
	if(colonne-1>3): #Partie droite du plateau on regarde l'alignement à gauche du pion
		if(plateau[colonne-1][5] == plateau[colonne-2][5] == plateau[colonne-3][5] == plateau[colonne-4][5] == player_turn):
			winner = player_turn
	elif(colonne-1<3): #Partie gauche du plateau on regarde l'alignement à droite du pion
		if(plateau[colonne-1][5] == plateau[colonne][5] == plateau[colonne+1][5] == plateau[colonne+2][5] == player_turn):
			winner = player_turn
	else: #Le pion est au milieu on regarde alignement à gauche et à droite du pion
		if(plateau[colonne-1][5] == plateau[colonne][5] == plateau[colonne+1][5] == plateau[colonne+2][5] == player_turn):
			winner = player_turn
		if(plateau[colonne-1][5] == plateau[colonne][5] == plateau[colonne+1][5] == plateau[colonne+2][5] == player_turn):
			winner = player_turn
	#Diagonales
	if(colonne-1>3): #Même principe si pion droite on regarde diag de bas vers haut gauche
		if(plateau[colonne-1][5] == plateau[colonne-2][4] == plateau[colonne-3][3] == plateau[colonne-4][2] == player_turn):
			winner = player_turn
	elif(colonne-1<3): #Inversement
		if(plateau[colonne-1][5] == plateau[colonne][4] == plateau[colonne+1][3] == plateau[colonne+2][2] == player_turn):
			winner = player_turn
	else : #Les deux
		if(plateau[colonne-1][5] == plateau[colonne-2][4] == plateau[colonne-3][3] == plateau[colonne-4][2] == player_turn):
			winner = player_turn
		if(plateau[colonne-1][5] == plateau[colonne][4] == plateau[colonne+1][3] == plateau[colonne+2][2] == player_turn):
			winner = player_turn
	return winner


def top10Main():
	plateau =[ [modele.VIDE for j in range(6)] for i in range(7) ]
	#JRJRJRJ
	for colonne in range(4):
		plateau[2*colonne][5] = modele.J1
	for colonne in range(3):
		plateau[2*colonne+1][5] = modele.J2
	#RJRJRJR
	for colonne in range(4):
		plateau[2*colonne][4] = modele.J2
	for colonne in range(3):
		plateau[2*colonne+1][4] = modele.J1
	#JRJRJRJ
	for colonne in range(4):
		plateau[2*colonne][3] = modele.J1
	for colonne in range(3):
		plateau[2*colonne+1][3] = modele.J2
	#RJRJRJR
	for colonne in range(4):
		plateau[2*colonne][2] = modele.J2
	for colonne in range(3):
		plateau[2*colonne+1][2] = modele.J1
	#JRJRJRJ
	for colonne in range(4):
		plateau[2*colonne][1] = modele.J1
	for colonne in range(3):
		plateau[2*colonne+1][1] = modele.J2
	#RJRJRJR
	for colonne in range(4):
		plateau[2*colonne][0] = modele.J2
	for colonne in range(3):
		plateau[2*colonne+1][0] = modele.J1
	player_turn = 0
	pionsJ1 = 0
	pionsJ2 = 0
	while(pionsJ1<=9 and pionsJ2<=9):	
		fin_Tour = False
		while not fin_Tour:
			affichage.effacerEcran()
			affichage.afficherRectangle()
			affichage.afficherCellule(plateau)
			print("")
			print("C'est le tour du joueur",player_turn+1)
			if(player_turn == 0):
				if(pionsJ1 == 0):
					print("")
					print("Vous n'avez aucun pion")
					print("")
				else :
					print("")
					print("Vous avez",pionsJ1,"pion(s)")
					print("")
			else:
				if(pionsJ2 == 0):
					print("")
					print("Vous n'avez aucun pion")
					print("")
				else:
					print("")
					print("Vous avez",pionsJ2,"pion(s)")
					print("")
			colonne = modeleDehors.selectColumnEject(plateau, player_turn)
			winner = winCheckTop10(plateau, colonne, player_turn)
			if(winner == player_turn): # Le pion appartient à une rangée de 4
				affichage.effacerEcran()
				affichage.afficherRectangle()
				affichage.afficherCellule(plateau)
				modeleDehors.ejectPawn(colonne, plateau)
				if(player_turn == 0):
					pionsJ1 = pionsJ1 + 1
				else :
					pionsJ2 = pionsJ2 + 1
			else: #Le pion n'appartient pas à une rangée de 4
				affichage.effacerEcran()
				affichage.afficherRectangle()
				affichage.afficherCellule(plateau)
				modeleDehors.ejectPawn(colonne, plateau)
				affichage.afficherCellule(plateau)
				x = colonne
				print("")
				print("C'est le tour du joueur",player_turn+1)
				if(player_turn == 0):
					if(pionsJ1 == 0):
						print("")
						print("Vous n'avez aucun pion")
						print("")
					else :
						print("")
						print("Vous avez",pionsJ1,"pion(s)")
						print("")
				else:
					if(pionsJ2 == 0):
						print("")
						print("Vous n'avez aucun pion")
						print("")
					else:
						print("")
						print("Vous avez",pionsJ2,"pion(s)")
						print("")
				colonne = selectColumnTop10(plateau, x) #Il remet son pion dans une colonne différente de celle du pion tiré
				modele.assignPawn(plateau, player_turn, colonne)
				fin_Tour = True
				player_turn = (player_turn+1)%2
	if(pionsJ1 == 10):
		print("FIN DE LA PARTIE, LE JOUEUR 1 A GAGNÉ")
	else :
		print("FIN DE LA PARTIE, LE JOUEUR 2 A GAGNÉ")




