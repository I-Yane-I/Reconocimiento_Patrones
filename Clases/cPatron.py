class cPatron():
    def __init__(self, caracteristicas: list[float] = None, etiqueta: str = ""):
        self.caracteristicas = caracteristicas if caracteristicas is not None else []
        self.etiqueta = etiqueta if etiqueta != "" else "etiqueta no definida"

    def imprimirPatron(self):
        for valor in self.caracteristicas:
            print(valor)
        print(self.etiqueta)


    def pruebaHola(self) -> None:
            print("hola mundo")