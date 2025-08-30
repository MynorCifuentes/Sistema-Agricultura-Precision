class Celda:
    """
    Representa una celda dentro de una fila de la matriz.
    Guarda: id del sensor (columna), valor (frecuencia) y enlaces doblemente enlazados.
    """
    def __init__(self, sensor_id: str, valor: int):
        self.sensor_id = sensor_id
        self.valor = valor
        self.siguiente = None
        self.anterior = None