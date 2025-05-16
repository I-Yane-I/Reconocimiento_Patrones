from Clases import CClases
import Clases.Lector_Patrones as lp
import Funcionalidades.Calcular_Distancias.euclidiana as ec
import Funcionalidades.Calcular_Distancias.Manhattan as ma
from Clases import cPatron

def  Reconocer(patron:cPatron,clase:CClases,tipoDistancia:str)-> str:
    minDista=0

    for i in clase:
        distancia=0
        if tipoDistancia=="euclidiana":
            ec.Calcular_Euclidiana(patron,clase.patron[i])
        else:
            ma.Manhattan(patron,clase[i])


print("hola pinches putas")


