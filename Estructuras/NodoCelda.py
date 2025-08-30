class Celda:
    def __init__(self, idSensor=None, idEstacion=None, frecuencia=None):
        self.idSensor = idSensor      # Columna
        self.idEstacion = idEstacion  # Fila
        self.frecuencia = frecuencia  # Valor