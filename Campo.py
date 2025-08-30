from Matriz import Matriz

class Campo:
    def __init__(self, id_campo, nombre):
        self.id = id_campo
        self.nombre = nombre
        self.matriz_suelo = Matriz(f"Suelo_{id_campo}")
        self.matriz_cultivo = Matriz(f"Cultivo_{id_campo}")

    def imprimir(self):
        print(f"\n===== Campo {self.id} - {self.nombre} =====")
        self.matriz_suelo.imprimir()
        self.matriz_cultivo.imprimir()