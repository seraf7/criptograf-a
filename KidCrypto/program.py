def KidCrypto():
    #Lectura de datos
    op = input()
    a = int(input())
    b = int(input())
    A = int(input())
    B = int(input())
    msj = int(input())

    #Validar que se cumplan con restricciones
    if(a == 1 and b == 1):
        print("Valores no soportados")
        return

    #Validacion de operacion a realizar
    if(op == 'E'):
        cifrar(a, b, A, B, msj)
    else:
        descifrar(a, b, A, B, msj)

#Funcion para calcular llaves
def llaves(a, b, A, B):
    #Calculo de M
    M = a*b - 1
    #Calculo de e
    e = A*M + a
    #Calculo de d
    d = B*M + b
    #Calculo de n
    n = (e*d - 1) // M
    #Retorno de valores
    return n, e, d

#Funcion de cifrado
def cifrar(a, b, A, B, x):
    n, e, d = llaves(a, b, A, B)
    #Obtencion del mensaje cifrado
    c = (x * e) % n
    print(c)
    return

#Funcion de descifrado
def descifrar(a, b, A, B, y):
    n, e, d = llaves(a, b, A, B)
    #Obtencion del mensaje original
    msj = (y * d) % n
    print(msj)
    return

#Llamado funcion principal del algoritmo
KidCrypto()
