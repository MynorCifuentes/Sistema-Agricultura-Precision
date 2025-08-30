from Estructuras.ListaDoble import ListaDoble
from Estructuras.ListaSimple import ListaSimple
from Estructuras.NodoCelda import Celda

class Matriz:
    def __init__(self, nombre="Matriz"):
        self.nombre = nombre
        self.filas = ListaDoble()         # Filas = estaciones
        self.estaciones = ListaSimple()   # Solo IDs (string)
        self.sensores = ListaSimple()     # Solo IDs (string)

    def agregar_estacion(self, idEstacion):
        if self.estaciones.buscar(idEstacion, atributo=None) is None:
            self.estaciones.agregarUltimo(idEstacion)
        if self.filas.buscar(idEstacion) is None:
            self.filas.agregarUltimo(idEstacion)

    def agregar_sensor(self, idSensor):
        if self.sensores.buscar(idSensor, atributo=None) is None:
            self.sensores.agregarUltimo(idSensor)

    def agregar_valor(self, idEstacion, idSensor, frecuencia):
        self.agregar_estacion(idEstacion)
        self.agregar_sensor(idSensor)
        nodo_fila = self.filas.buscar(idEstacion)
        celda_existente = nodo_fila.fila.buscar(idSensor, "idSensor")
        if celda_existente is not None:
            celda_existente.dato.frecuencia = frecuencia
        else:
            nueva_celda = Celda(idSensor=idSensor, idEstacion=idEstacion, frecuencia=frecuencia)
            nodo_fila.fila.agregarUltimo(nueva_celda)

    def completar_ceros(self):
        temp_est = self.estaciones.primero
        while temp_est is not None:
            idEstacion = temp_est.dato
            nodo_fila = self.filas.buscar(idEstacion)
            temp_sens = self.sensores.primero
            while temp_sens is not None:
                idSensor = temp_sens.dato
                celda_existente = nodo_fila.fila.buscar(idSensor, "idSensor")
                if celda_existente is None:
                    nueva_celda = Celda(idSensor=idSensor, idEstacion=idEstacion, frecuencia="0")
                    nodo_fila.fila.agregarUltimo(nueva_celda)
                temp_sens = temp_sens.siguiente
            temp_est = temp_est.siguiente

    def imprimir(self):
        print("\n" + self.nombre + ":")
        # Imprime encabezado de sensores
        print("      ", end="")
        temp_sens = self.sensores.primero
        while temp_sens is not None:
            print("  " + str(temp_sens.dato), end="")
            temp_sens = temp_sens.siguiente
        print()
        # Imprime filas (estaciones)
        temp_est = self.estaciones.primero
        while temp_est is not None:
            print(" " + str(temp_est.dato), end=":")
            nodo_fila = self.filas.buscar(temp_est.dato)
            temp_sens = self.sensores.primero
            while temp_sens is not None:
                celda = None
                if nodo_fila is not None:
                    celda_nodo = nodo_fila.fila.buscar(temp_sens.dato, "idSensor")
                    if celda_nodo is not None:
                        celda = celda_nodo.dato
                if celda is not None and celda.frecuencia is not None:
                    print("  " + str(celda.frecuencia), end="")
                else:
                    print("  0", end="")
                temp_sens = temp_sens.siguiente
            print()
            temp_est = temp_est.siguiente

    def graficar(self, nombre_archivo, nombre_img):
        self.filas.graficar(nombre_archivo, nombre_img, self.sensores)