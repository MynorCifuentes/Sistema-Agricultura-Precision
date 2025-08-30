from Estructuras.ListaSimple import ListaSimple
import os

class NodoEncabezado:
    def __init__(self, idEstacion=None):
        self.idEstacion = idEstacion
        self.siguiente = None
        self.anterior = None
        self.fila = ListaSimple()

class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def estaVacio(self):
        return self.primero == self.ultimo == None

    def agregarUltimo(self, idEstacion):
        nuevo = NodoEncabezado(idEstacion=idEstacion)
        if self.estaVacio():
            self.primero = self.ultimo = nuevo
        else:
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
        self.tamanio += 1
        return nuevo

    def buscar(self, idEstacion):
        temp = self.primero
        while temp is not None:
            if temp.idEstacion == idEstacion:
                return temp
            temp = temp.siguiente
        return None

    def recorrer(self, sensores):
        temp = self.primero
        while temp is not None:
            print(f"Estación {temp.idEstacion}: ", end="")
            temp.fila.recorrer()
            temp = temp.siguiente

    def graficar(self, nombre_archivo, nombre_img, sensores):
        carpeta = os.path.dirname(nombre_archivo)
        if carpeta and not os.path.exists(carpeta):
            os.makedirs(carpeta)
        contenido = """
graph G {
  node [shape=plaintext];
  matriz [label=<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" >
"""
        temp = self.primero
        while temp is not None:
            contenido += "<TR>"
            contenido += f'<TD WIDTH="50" HEIGHT="50">{temp.idEstacion}</TD>'
            contenido += temp.fila.graficarCelda(sensores)
            contenido += "</TR>\n"
            temp = temp.siguiente
        contenido += """
    </TABLE>
  >];
}
"""
        with open(nombre_archivo, "w", encoding="utf-8") as file:
            file.write(contenido)
        os.system(f"dot -Tpng {nombre_archivo} -o {nombre_img}")
        print("Gráfica generada exitosamente en la carpeta Salidas.")