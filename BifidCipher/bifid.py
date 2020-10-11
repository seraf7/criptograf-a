tableau = [[], [], [], [], []]

def Bifid():
	key = "ENCRYPT"
	tableau = genTableau(key)
	op = input()
	msj = input()
	#Limpieza de la cadena
	msj = msj.replace(' ', '')
	#Valida la operación a realizar
	if(op == "ENCRYPT"):
		encriptar(msj)
	elif(op == "DECRYPT"):
		desencriptar(msj)
	else:
		return

#Generacion de la tabla
def genTableau(key):
	global tableau
	alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
	i = 0
	k = 0
	for r in range(5):
		for c in range(5):
			#Valida si se han ingresado todas las letras de key
			if k < len(key):
				tableau[r].append(key[k])
				k += 1
			else:
				#Salta la letras que se encuentran en key
				while alfabeto[i] in key:
					i += 1
				tableau[r].append(alfabeto[i])
				i += 1
	return tableau

def buscaIndice(l):
	x = 0
	global tableau
	for r in range(len(tableau)):
		if l in tableau[r]:
			x = r
			break
	y = tableau[x].index(l)
	return x, y

#Funcion para obtener una matriz con los indices del mensaje
def indices(msj):
	M = [[], []]
	for i in range(len(msj)):
		x, y = buscaIndice(msj[i])
		M[0].append(x)
		M[1].append(y)
	return M

def buscaLetra(r, c):
	global tableau
	return tableau[r][c]

#Funcion para obtener los caracteres de una matriz de indices
def letras(C):
	crip = ""
	for i in range(len(C[0])):
		crip = crip + buscaLetra(C[0][i], C[1][i])
	return crip

def encriptar(msj):
	L = []
	C = [[], []]
	M = indices(msj)
	for r in range(len(M)):
		for c in range(len(M[0])):
			L.append(M[r][c])
	for i in range(0, len(L), 2):
		C[0].append(L[i])
		C[1].append(L[i+1])
	crip = letras(C)
	print(crip)

def desencriptar(crip):
	L = []
	M = [[], []]
	C = indices(crip)
	for i in range(len(C[0])):
		L.append(C[0][i])
		L.append(C[1][i])
	for i in range(int(len(L)/2)):
		M[0].append(L[i])
	for i in range(int(len(L)/2), len(L)):
		M[1].append(L[i])
	msj = letras(M)
	print(msj)

Bifid()
