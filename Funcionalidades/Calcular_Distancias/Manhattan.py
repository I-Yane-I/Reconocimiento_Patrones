import math
from Clases import cPatron

def Manhattan(patron1:cPatron,patron2:cPatron) -> float:
    carac1=patron1.caracteristicas
    carac2=patron2.caracteristicas

    if len(carac1)!=len(carac2):
        raise ValueError("los patrones deben ser de la misma dimension")
    suma=0.0
    for valor in range(len(carac1)):
        suma += abs(carac1[valor]-carac2[valor])
    return suma
