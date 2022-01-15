
from colorama import Fore, Back, Style
import modele


def effacerEcran():
    print("\x1b[2J\x1b[H")
    
def posXY(abscisse, ordonnee):
    absc = str(abscisse)
    ordo = str(ordonnee)
    print("\x1b["+ordo+";"+absc+"H",sep="",end="")

def afficherRectangle():
	print(Fore.BLACK)
	for abs in range((modele.LARGEUR*7)+1):
		for ord in range((modele.HAUTEUR*4)+1):
			posXY(abs+3, ord+2)
			print(Back.BLUE, Fore.WHITE, "  ",end="",sep="")
	posXY(6,26)
	print("1")
	posXY(13,26)
	print("2")
	posXY(20,26)
	print("3")
	posXY(27,26)
	print("4")
	posXY(34,26)
	print("5")
	posXY(41,26)
	print("6")
	posXY(48,26)
	print("7")
	posXY(1,1)
	print(Back.BLACK, Fore.WHITE, sep="", end="")

def afficherCellule(plateau):
	for abs in range(modele.LARGEUR):
		for ord in range(modele.HAUTEUR):
			if(plateau[abs][ord] == modele.VIDE):
				posXY(((abs*7)+5),(((ord*4)+4)))
				print(Back.BLACK,"  ")
			elif(plateau[abs][ord] == modele.J1):
				posXY(((abs*7)+5),(((ord*4)+4)))
				print("\U0001F7E1 ",sep="",end="")#Pion jaune
			elif(plateau[abs][ord] == modele.J2):
				posXY(((abs*7)+5),(((ord*4)+4)))
				print("\U0001F534 ",sep="",end="")#Pion rouge
	print("")
	print("")
	print("")