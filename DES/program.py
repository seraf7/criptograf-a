def DES():
	op = input()
	key = input()
	msj = input()

	#Validar la operacion a realizar
	if(op == 'E'):
		#Operacion de cifrad
		Encriptar(key, msj)
	elif(op == 'D'):
		#Operacion de descifrado
		Desencriptar(key, msj)
	return

#Función de permutación inicial
def permutacionInicial(m):
	p = m[1] + m[5] + m[2] + m[0] + m[3] + m[7] + m[4] + m[6]
	return p

def permutacionInversa(m):
	p = m[3] + m[0] + m[2] + m[4] + m[6] + m[1] + m[7] + m[5]
	return p

#Funcion de desplazamiento cíclico
def rotarIzq(k, n):
	return k[n:] + k[:n]

#Funcion para generar subllave
def genSubllave(key):
	k = key[5] + key[2] + key[6] + key[3] + key[7] + key[4] + key[9] + key[8]
	return k

#Funcion para generar subllaves
def subllaves(k):
	#Permutacion de caracteres
	key = k[2] + k[4] + k[1] + k[6] + k[3] + k[9] + k[0] + k[8] + k[7] + k[5]
	#Rotacion de 1 bit las dos mitades
	key = rotarIzq(key[:5], 1) + rotarIzq(key[5:], 1)
	#Generacion de subllave 1
	k1 = genSubllave(key)
	#Rotacion de 2 bit las dos mitades
	key = rotarIzq(key[:5], 2) + rotarIzq(key[5:], 2)
	#Generacion de subllave 2
	k2 = genSubllave(key)
	return k1, k2

def expansion(m):
	mExp = m[3] + m[0] + m[1] + m[2] + m[1] + m[2] + m[3] + m[0]
	return mExp

#Funcion de mezclado con S-Box 0
def sBoxS0(m):
	#Definicion de S-box S0
	S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
	r = int(m[0]+m[3], 2)
	c = int(m[1:3], 2)
	S = "{0:0>2b}".format(S0[r][c])
	return S

#Funcion de mezclado con S-Box 1
def sBoxS1(m):
	#Definicion de S-box S1
	S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]
	r = int(m[0]+m[3], 2)
	c = int(m[1:3], 2)
	S = "{0:0>2b}".format(S1[r][c])
	return S

def Feistel(m, k):
	#Dividir el mensaje en dos mitades
	mI = m[:int(len(m)/2)]
	mD = m[int(len(m)/2):]
	#Expansion de mitad derecha
	mD = expansion(mD)
	#Operacion XOR con la llave
	mD = int(mD, 2) ^ int(k, 2)
	#Representacion de 8 bits de la operacion
	mD = "{0:0>8b}".format(mD)
	#Transformacion con S-Box con cada mitad y concatenacion
	mD = sBoxS0(mD[:int(len(mD)/2)]) + sBoxS1(mD[int(len(mD)/2):])
	#Permutacion del resultado obtenido
	mD = mD[1] + mD[3] + mD[2] + mD[0]
	#Operación XOR con la mitad izquierda
	mI = int(mD, 2) ^ int(mI, 2)
	#Representacion de 4 bits de la operacion
	mI = "{0:0>4b}".format(mI)
	#Concatenar con mitad derecha original
	return mI + m[int(len(m)/2):]

#Funcion para encriptar el mensaje
def Encriptar(key, msj):
	#Generacion de subllaves
	k1, k2 = subllaves(key)
	#Permutacion inicial
	c = permutacionInicial(msj)
	#Paso Feistel con subllave 1
	c = Feistel(c, k1)
	#Intercambiar mitades
	c = rotarIzq(c, int(len(c)/2))
	#Paso Feistel con subllave 2
	c = Feistel(c, k2)
	#Permutacion inversa
	c = permutacionInversa(c)
	print(c)
	return

#Funcion para encriptar el mensaje
def Desencriptar(key, msj):
	#Generacion de subllaves
	k1, k2 = subllaves(key)
	#Permutacion inicial
	m = permutacionInicial(msj)
	#Paso Feistel con subllave 2
	m = Feistel(m, k2)
	#Intercambiar mitades
	m = rotarIzq(m, int(len(m)/2))
	#Paso Feistel con subllave 1
	m = Feistel(m, k2)
	#Permutacion inversa
	m = permutacionInversa(m)
	print(m)
	return

#Llamada del algoritmo general
DES()