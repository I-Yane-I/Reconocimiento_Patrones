class cPatron():
    def __init__(self, caracteristicas: list[float], etiqueta: str = "") -> None:
        self.caracteristicas = caracteristicas
        self.etiqueta = etiqueta


    def imprimirPatron(self) -> None:
        for valor in self.caracteristicas:
            print(valor)



