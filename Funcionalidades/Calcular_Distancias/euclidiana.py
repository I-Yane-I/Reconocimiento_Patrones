import math
from Clases import cPatron

def Calcular_Euclidiana(patron1: cPatron, patron2:cPatron) -> float:
    carac1=patron1.caracteristicas
    carac2=patron2.caracteristicas
    aux=1                                           # Para que siempre apunte al contenido de la tupla ["fruta",(1,1,1)]
    if len(carac1)!=len(carac2):
        raise ValueError("los patrones deben ser de la misma dimension")
    suma=0.0
    for valor in range(len(carac1)):
        suma +=pow(carac1[valor]-carac2[valor],2)
    return math.sqrt(suma)

