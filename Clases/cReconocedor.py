import cPatron
from Funcionalidades.Calcular_Distancias.euclidiana import Calcular_Euclidiana
from Funcionalidades.Calcular_Distancias.Manhattan import calcular_Manhattan

from typing import List

class Reconecedor():
  def __init__(self, patron: cPatron, lista_patrones: List[cPatron], tipo_distancia: str):
    self.patron = cPatron()
    self.lista_patrones = [cPatron()]
    self.tipo_distancia = tipo_distancia.lower() 
  etiquetaCercana=""
  Distancia:List[float]
  
  minDistancia: Distancia = [] # type: ignore
  for patron in range(len(lista_patrones)):
    distancia=0
    if self.tipo_distancia=="euclidiana":
      distancia=Calcular_Euclidiana(self.patron,patron)
    elif self.tipo_distancia == "manhattan":
      distancia =calcular_Manhattan(self.patron, patron)
    if distancia<minDistancia:
      minDistancia=distancia
      etiquetaCercana=patron.etiqueta