#affichageDefi.py

from colorama import Fore, Back, Style
import affichage
import modele
import modeleDefi

def afficherCelluleDefi(plateau):
	for abs in range(modele.LARGEUR):
		for ord in range(modele.HAUTEUR):
			if(plateau[abs][ord] == modele.VIDE):
				affichage.posXY(((abs*7)+5),(((ord*4)+4)))
				print(Back.BLACK,"  ")
			elif(plateau[abs][ord] == modele.J1):
				affichage.posXY(((abs*7)+5),(((ord*4)+4)))
				print("\U0001F7E1 ",sep="",end="")#Pion jaune
			elif(plateau[abs][ord] == modele.J2):
				affichage.posXY(((abs*7)+5),(((ord*4)+4)))
				print("\U0001F534 ",sep="",end="")#Pion rouge
			elif(plateau[abs][ord] == modeleDefi.ENCLUME):
				affichage.posXY(((abs*7)+5),(((ord*4)+4)))
				print("\U0001F1EA  ",sep="",end="")
			elif(plateau[abs][ord] == modeleDefi.MUR):
				affichage.posXY(((abs*7)+5),(((ord*4)+4)))
				print("\U0001F1F2  ",sep="",end="")
			elif(plateau[abs][ord] == modeleDefi.X2):
				affichage.posXY(((abs*7)+5),(((ord*4)+4)))
				print("\U0001F1FD  ",sep="",end="")
			elif(plateau[abs][ord] == modeleDefi.BRISEUR):
				affichage.posXY(((abs*7)+5),(((ord*4)+4)))
				print("\U0001F4A3  ",sep="",end="")
	print("")
	print("")
	print("")
