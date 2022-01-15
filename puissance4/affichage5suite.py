#affichage5suite.py

from colorama import Fore, Back, Style
import modele
import modele5suite
import affichage


def afficherRectangle5suite():
	print(Fore.BLACK)
	for abs in range((modele5suite.LARGEUR5suite*7)+1):
		for ord in range((modele5suite.HAUTEUR5suite*4)+1):
			affichage.posXY(abs+3, ord+2)
			print(Back.BLUE, Fore.WHITE, "  ",end="",sep="")
	affichage.posXY(13,26)
	print("1")
	affichage.posXY(20,26)
	print("2")
	affichage.posXY(27,26)
	print("3")
	affichage.posXY(34,26)
	print("4")
	affichage.posXY(41,26)
	print("5")
	affichage.posXY(48,26)
	print("6")
	affichage.posXY(55,26)
	print("7")
	affichage.posXY(1,1)
	print(Back.BLACK, Fore.WHITE, sep="", end="")

def afficherCellule5suite(plateau):
	for abs in range(modele5suite.LARGEUR5suite):
		for ord in range(modele5suite.HAUTEUR5suite):
			if(plateau[abs][ord] == modele.VIDE):
				affichage.posXY(((abs*7)+5),(((ord*4)+4)))
				print(Back.BLACK,"  ")
			elif(plateau[abs][ord] == modele.J1):
				affichage.posXY(((abs*7)+5),(((ord*4)+4)))
				print("\U0001F7E1 ",sep="",end="")#Pion jaune
			elif(plateau[abs][ord] == modele.J2):
				affichage.posXY(((abs*7)+5),(((ord*4)+4)))
				print("\U0001F534 ",sep="",end="")#Pion rouge
	print("")
	print("")
	print("")