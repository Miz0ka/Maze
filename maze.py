import numpy as np
import random as rand
import matplotlib.pyplot as plt 

#Il est important d'avoir une idee breve de ce que fait l'algo
#Si le texte le suffit pas: https://commons.wikimedia.org/wiki/File:Yl_maze_ani_algo1.gif?uselang=fr
#Desoler pour les fautes d'orthographe
#Pas d'accent pour evite les problemes d'encodage

def init(n):
	"""
	Prend en entrer une variable correspondent a un entier et retourne\n
	une matrice numpy de dimension n*n ainsi qu'un tableau resensent\n
	les murs chaque valeur est de la forme (x,y)(x',y')
	"""
	#Genere la matrice avec chaque case une valeur diff (Commence pas a Zero, pas cherche a le faire apparaitre
	celule=np.array([[0 for i in range(n)] for j in range(n)])
	x=0
	for i in range(n):
		for j in range(n):
			celule[i,j]=x
			x+=1
	mur=[]
	#Valeur qui varie de 0 a 1 de manier a test tout les valeurs	
	#Un mur sur les cases (1,1)(0,1) <=> (0,1)(1,1)
	#Donc tout les valeurs sont traiter 
	di=1 
	dj=0
	for temp in range(2): #Deux valeurs sur di et dj
		for i in range (n):
			for j in range(n):
				if (i+di<n) and (j+dj<n):
					mur.append(((i,j),(i+di,j+dj)))
		#modifier le append pour avoir un format plus simple
		di= 1 - di # Passe de 1 a 0
		dj= 1 - dj # Passe de 0 a 1


	return celule, mur


def casseMur(indice, listeMur, matrice):
	"""
	Retire un mur de la liste des murs s'il separe deux zone differente 
	Entre: indice=int
	"""
	c,c1=listeMur[indice] #Manier de gere Mur pas tres pratique a modifier car listeMur[indice] renvoie deux tuples, il faut ensuite vide les tuples
	x,y = c #Vide les tuples
	x1,y1 = c1 #Vide les tuples
	if (matrice[x,y] != matrice[x1,y1]): #Si zone diff
		listeMur.pop(indice)
		matrice = changeValeur(matrice[x,y],matrice, x1,y1)
	return matrice

def changeValeur(entier, matrice, x,y):
	"""
	Quand on detruit un mur, on met a la meme valeur les deux cote du mur	
	"""
	#Code de manier tres simple mais tres gourmant si grand tableau
	#Il est specifier par le prof qu'il vous attend sur la manier de faire cette partie, soit vous essayez soit je vous donne un soluce 	
	#A modifier
	tmp=matrice[x,y]
	n,m=matrice.shape
	for i in range(n):
		for j in range(m):
			if (matrice[i,j]==tmp):
				matrice[i,j]=entier
	return(matrice)

def check(matrice):
	"""
	Renvoie true si tout les cases sont uniformiser
	Sinon false
	"""
	exit=True
	tmp=matrice[0,0]
	n,m=matrice.shape
	for i in range(n):
		for j in range(m):
			if (matrice[i,j] != tmp):
				exit=False
				break
		if (not(exit)):
			break
	return(exit)

def affiche(matrice):
	"""
	Affichage pour avoir moins d'info
	"""
	n,m=matrice.shape
	print("")
	for i in range(n):
		print(matrice[i])

def fusion(n,mur):
	"""
	Prend en entree un entier correspondant au nombre de cellule par ligne et une liste de mur
	Sortie: Le labyrinthe
	"""
	#Ajout des murs qui n'existe qu'en diagonal les fameux 1 en rouge
	di=1
	dj=1
	for i in range (n):
		for j in range(n):
			if (i+di<n) and (j+dj<n):
				mur.append(((i,j),(i+di,j+dj)))
	#On augmente la taille pour accueilir les murs	
	n = n*2 - 1 #il y a n-1 ligne de mur, un dessin le montre bien
	matrice=np.zeros((n,n)) #La version final manque que les murs
	for i in mur: #du a la forme chiante de murMaze, a modifier pour simplifier
		i1,i2=i
		x,y=i1
		x1,y1=i2
		x2=(x1+x)#*2/2
		y2=(y1+y)# Donc voila en gros les coordonne sont tous multiplier par deux et le mur sont donc entre deux de ces cases, on recupe donc le millieu pour avoir les coordonnees des murs
		matrice[x2,y2]=1 #On place le mur
	return matrice

def mazeGenerator():
	n = int(input("Nombre de cellule:\n\t"))
	maze, murMaze = init(n)
	while(not(check(maze))): #Tant que tout les cases n'ont pas la meme valeur
		indice=rand.randrange(len(murMaze)-1) #-1 pour evite le outrange
		maze=casseMur(indice, murMaze, maze)

	maze=fusion(n,murMaze)
	#affiche(maze)
	
	plt.matshow(maze, fignum=0, cmap=plt.cm.gray)
	plt.show()
		
mazeGenerator()	
