class cPatron():
    def __init__(self, caracteristicas: list[float]) -> None:
        self.caracteristicas = caracteristicas


    def imprimirPatron(self) -> None:
        for valor in self.caracteristicas:
            print(valor)

    def getCaracteristicas(self)->"caracteristicas":
        return self.caracteristicas

