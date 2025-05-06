import cPatron
from Funcionalidades.Calcular_Distancias import euclidiana , Manhattan
from typing import List

class Reconecedor():
      def __init__(self, patron: cPatron, lista_patrones: List[cPatron], tipo_distancia: str):
        self.patron = patron
        self.lista_patrones = lista_patrones
        self.tipo_distancia = tipo_distancia.lower() 
    