#Definicion de S
S = [
  41, 46, 67, 201, 162, 216, 124, 1, 61, 54, 84, 161, 236, 240, 6,
  19, 98, 167, 5, 243, 192, 199, 115, 140, 152, 147, 43, 217, 188,
  76, 130, 202, 30, 155, 87, 60, 253, 212, 224, 22, 103, 66, 111, 24,
  138, 23, 229, 18, 190, 78, 196, 214, 218, 158, 222, 73, 160, 251,
  245, 142, 187, 47, 238, 122, 169, 104, 121, 145, 21, 178, 7, 63,
  148, 194, 16, 137, 11, 34, 95, 33, 128, 127, 93, 154, 90, 144, 50,
  39, 53, 62, 204, 231, 191, 247, 151, 3, 255, 25, 48, 179, 72, 165,
  181, 209, 215, 94, 146, 42, 172, 86, 170, 198, 79, 184, 56, 210,
  150, 164, 125, 182, 118, 252, 107, 226, 156, 116, 4, 241, 69, 157,
  112, 89, 100, 113, 135, 32, 134, 91, 207, 101, 230, 45, 168, 2, 27,
  96, 37, 173, 174, 176, 185, 246, 28, 70, 97, 105, 52, 64, 126, 15,
  85, 71, 163, 35, 221, 81, 175, 58, 195, 92, 249, 206, 186, 197,
  234, 38, 44, 83, 13, 110, 133, 40, 132, 9, 211, 223, 205, 244, 65,
  129, 77, 82, 106, 220, 55, 200, 108, 193, 171, 250, 36, 225, 123,
  8, 12, 189, 177, 74, 120, 136, 149, 139, 227, 99, 232, 109, 233,
  203, 213, 254, 59, 0, 29, 57, 242, 239, 183, 14, 102, 88, 208, 228,
  166, 119, 114, 248, 235, 117, 75, 10, 49, 68, 80, 180, 143, 237,
  31, 26, 219, 153, 141, 51, 159, 17, 131, 20
]

def MD2():
	m = input()
	m = ascii(m)
	m = Padding(m)
	m = Checksum(m)
	m = Hash(m)
	imprimir(m)

#Conversión de texto a sus valores ASCII
def ascii(m):
	r = []
	if(m == '""'):
		return r
	for i in range(len(m)):
		#Valor ASCII de cada caracter
		r.append(ord(m[i]))
	return r

def Padding(m):
	#Determinar cantidad de elementos a agregar y byte de padding
	p = 16 - (len(m) % 16)
	#Añadir valores de relleno
	for i in range(p):
		#Añade byte al final del mensaje
		m.append(p)
	return m

def Checksum(M):
	#Inicializacion de variables
	N = len(M)
	C = 16 * [0]
	L = 0
	for i in range(int(N/16)):
		for j in range(16):
			c = M[16 * i + j]
			C[j] = C[j] ^ S[c^L]
			L = C[j]
	#Extender lista con 16 bytes de checksum
	M.extend(C)
	return M

def Hash(M):
	#Inicializacion de variables
	X = 48 * [0]
	N = len(M)
	for i in range(int(N/16)):
		for j in range(16):
			X[j+16] = M[16 * i + j]
			X[j+32] = X[j+16] ^ X[j]
		t = 0
		for j in range(18):
			for k in range(48):
				t = X[k] ^ S[t]
				X[k] = t
			t = (t+j) % 256
	return X

def imprimir(X):
	#Inicializacion de la cadena
	h = ''
	for i in range(16):
		#Concatenar representacion hexadecimal del elemento
		h += "{0:0>2x}".format(X[i])
	print(h)
	return

#Lalmado a la funcion principal
MD2()