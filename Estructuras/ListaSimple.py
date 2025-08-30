class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None

class ListaSimple:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def estaVacia(self):
        return self.primero is None

    def agregarUltimo(self, dato):
        nuevo = Nodo(dato=dato)
        if self.estaVacia():
            self.primero = self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
        self.tamanio += 1

    def buscar(self, valor, atributo=None):
        temp = self.primero
        while temp is not None:
            if atributo is None:
                if temp.dato == valor:
                    return temp
            else:
                if hasattr(temp.dato, atributo):
                    if getattr(temp.dato, atributo) == valor:
                        return temp
            temp = temp.siguiente
        return None

    def recorrer(self):
        temp = self.primero
        while temp is not None:
            print(str(temp.dato), end=" | ")
            temp = temp.siguiente
        print()

    def graficarCelda(self, sensores):
        cadena = ""
        temp_sens = sensores.primero
        while temp_sens is not None:
            idSensor = temp_sens.dato
            temp_celda = self.buscar(idSensor, "idSensor")
            freq = temp_celda.dato.frecuencia if temp_celda else "0"
            cadena += '<TD WIDTH="50" HEIGHT="50">' + str(freq) + '</TD>\n'
            temp_sens = temp_sens.siguiente
        return cadena