import re
from Crypto.Hash import SHA3_384
from time import time

#lista de tiempos
t = []

#Decorador para medir el tiempo
def tiempoTranscurrido(f):
    def wrapper(m):
        #Inicio del tiempo
        start = time()
        #Llamado a la funcion original
        ret = f(m)
        #Calcular tiempo transcurrido
        tiempo = time() - start
        t.append(tiempo)
        #print("Tiempo = %0.10f" % tiempo)
        return ret
    return wrapper

#Funcion para generar hashes
@tiempoTranscurrido
def mdHash(ms):
    #Creacion de objeto Hash
    h_obj = SHA3_384.new()
    #Generacion de hash
    h_obj.update(ms)
    #Impresion del hash en hexadecimal
    #print(h_obj.hexdigest())

def pruebaSha3():
    #Abrir archivo de vectores
    f = open('testSha/SHA3_512ShortMsg.rsp')
    #Lectura del archivo
    lineas = f.read()
    #print(lineas)

    #Expresion regular para obtener mensajes
    patron = re.compile(r'Msg = \w+')
    ms = patron.findall(lineas)
    #print(len(ms))

    #Generacion de cadenas de bytes de los mensajes
    for i in range(len(ms)):
        #Limpieza de la cedna
        ms[i] = ms[i].replace('Msg = ', '')
        ms[i] = bytes.fromhex(ms[i])
    #print(ms)

    for i in range(len(ms)):
        mdHash(ms[i])

    #Impresion de tiempos
    prom = 0
    for i in range(len(t)):
        print("Tiempo = %0.10f" % t[i])
        prom += t[i]

    print("Promedio = %0.10f" % (prom/len(t)))

pruebaSha3()
