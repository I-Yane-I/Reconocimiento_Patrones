class cPatron():
    def __init__(self,caracteristicas:list[float],etiqueta: str=""):
        self.caracteristicas=caracteristicas
        self.etiqueta=etiqueta if etiqueta !=""else "etiqueta no definida"


    def imprimirPatron(self):
        for valor in self.caracteristicas:
            print(valor+"")
        print(self.etiqueta)