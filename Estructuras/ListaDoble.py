from Celda import Celda

class ListaDoble:
    """
    Lista doblemente enlazada que almacena celdas (una fila de la matriz).
    Cada nodo (Celda) representa un sensor y su frecuencia.
    """
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None

    def buscar(self, sensor_id: str) -> Celda:
        aux = self.primero
        while aux is not None:
            if aux.sensor_id == sensor_id:
                return aux
            aux = aux.siguiente
        return None

    def insertar_o_actualizar(self, sensor_id: str, valor: int):
        existente = self.buscar(sensor_id)
        if existente:
            existente.valor = valor
            return

        nuevo = Celda(sensor_id, valor)

        # Inserción ordenada por sensor_id (opcional; facilita impresión ordenada)
        if self.esta_vacia():
            self.primero = self.ultimo = nuevo
            return

        # Si va al inicio
        if sensor_id < self.primero.sensor_id:
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo
            return

        # Si va al final
        if sensor_id > self.ultimo.sensor_id:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo
            return

        # Inserción intermedia
        actual = self.primero
        while actual is not None and actual.sensor_id < sensor_id:
            actual = actual.siguiente

        anterior = actual.anterior
        anterior.siguiente = nuevo
        nuevo.anterior = anterior