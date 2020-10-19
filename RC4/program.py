def RC4():
	key = input()
	mensaje = input()
	
	#Conversion de datos
	key = decimal(key)
	mensaje = decimal(mensaje)
	#Llamado al algoritmo KSA
	S = KSA(key)
	#Llamado al algoritmo PRGA
	keystream = PRGA(S, mensaje)
	#Generacion del texto cifrado
	cr = xoRed(keystream, mensaje)
	#Impresion de la cadena cifrada
	print(cadenaHexa(cr))


#Conversión de la llave a su representación decimal
def decimal(cadena):
	dec = []
	for i in range(len(cadena)):
	    dec.append(ord(cadena[i]))
	return dec

def KSA(key):
	#Inicialización del vector S
	S = [i for i in range(256)]

	#Bloque de permutación de S
	j = 0
	for i in range(len(S)):
	    j = (j + S[i] + key[i%(len(key))]) % 256
	    S[i], S[j] = S[j], S[i]
	return S

#Generación del keystream
def PRGA(S, mensaje):
	i = 0
	j = 0
	keystream = []
	for c in range(len(mensaje)):
	    i = (i + 1) % 256
	    j = (j + S[i]) % 256
	    S[i], S[j] = S[j], S[i]
	    keystream.append(S[(S[i] + S[j]) % 256])
	return keystream

#Generación del texto cifrado
def xoRed(keystream, mensaje):
	cr = []
	for i in range(len(mensaje)):
		#Operacion XOR con cada elemento
		cr.append(keystream[i] ^ mensaje[i])
	return cr

#Generacion de la cadena cifrada en valores Hexadecimales
def cadenaHexa(m):
	hexa = ""
	for i in range(len(m)):
		#Formateo para mantener siempre dos valores
		hexa += "{0:0>2X}".format(m[i])
	return hexa

#Llamado al algoritmo RC4
RC4()