import fileinput

def sumar(lista):
    suma = 0
    
    while lista:
        n = lista.pop()
        try:
        	n = int(n)
        except:
        	n = float(n)
        suma += n
    #Termina el ciclo e imprime
    print(suma)

lines = []
for line in fileinput.input():
    lines.append(line)

sumar(lines)
