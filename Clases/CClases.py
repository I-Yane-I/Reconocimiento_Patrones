import cPatron as P


class Clase:
    def __init__(self,patron:list[P],etiqueta:str)-> None:
        self.patron=patron
        self.etiqueta=etiqueta

    def agregarPatron(self,P:P.cPatron)-> None:
        self.patron.append(P)

    @staticmethod
    def crearClase(patron:list[float],etiqueta:str):
        NuevoP=[P.cPatron(patron)]

        return Clase(NuevoP, etiqueta)


    def imprimirClase(self) -> None:
        print(self.etiqueta)
        for i in self.patron:
            i.imprimirPatron()
            print(i.getCaracteristicas)

nueva_clase = Clase.crearClase([1,2,3], "Ejemplo")
print(nueva_clase.patron[0])  # Resultado: Ejemplo
