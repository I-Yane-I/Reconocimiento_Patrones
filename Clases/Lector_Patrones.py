
import numpy as np

def LeerConsola()-> list[float]:
    return list(map(float, input("Introduce un vector en R³ separado por espacios: ").split(" ",1)))

def LeerEtiquetas()-> list[str]:
    etiquetas=[]
    with open("../Patrones/patrones.txt","r") as nombres:
        for linea in nombres:
            etiqueta=linea.strip().split(" ",1)[0]
            etiquetas.append(etiqueta)
    return etiquetas



def LeerPatrones()-> list[float]:
    patrones = [float]  # Lista para almacenar los datos

    with open("../Patrones/patrones.txt", "r") as archivo:
        for linea in archivo:
            valores = linea.strip().split(" ", 1)[1]  # separa la fruta y el valor en arrays diferentes
            valores = np.array(eval(valores),dtype=float)  # evalue convierte valores a tupla (1,2,3)

            valores = np.append(valores, 1)  # si es r2 lo transforma a r3
            patrones.append(valores)  # Guardar en lista

    return patrones
