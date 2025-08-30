import xml.etree.ElementTree as ET
from Campo import Campo
from Estructuras.ListaSimple import ListaSimple

class Gestor:
    def __init__(self):
        self.campos = ListaSimple()
        self.cargado = False

    def limpiar(self):
        self.campos = ListaSimple()
        self.cargado = False

    def leer_archivo(self, ruta_entrada):
        self.limpiar()
        try:
            tree = ET.parse(ruta_entrada)
            root = tree.getroot()
            for campo_elem in root.findall("campo"):
                id_campo = campo_elem.get("id")
                nombre_campo = campo_elem.get("nombre")
                campo_obj = Campo(id_campo, nombre_campo)
                self.campos.agregarUltimo(campo_obj)

                # Recolecta estaciones y sensores
                estaciones_base = campo_elem.find("estacionesBase")
                if estaciones_base is not None:
                    for estacion_elem in estaciones_base.findall("estacion"):
                        id_est = estacion_elem.get("id")
                        campo_obj.matriz_suelo.agregar_estacion(id_est)
                        campo_obj.matriz_cultivo.agregar_estacion(id_est)

                sensores_suelo = campo_elem.find("sensoresSuelo")
                if sensores_suelo is not None:
                    for sensorS_elem in sensores_suelo.findall("sensorS"):
                        id_sensorS = sensorS_elem.get("id")
                        campo_obj.matriz_suelo.agregar_sensor(id_sensorS)

                sensores_cultivo = campo_elem.find("sensoresCultivo")
                if sensores_cultivo is not None:
                    for sensorT_elem in sensores_cultivo.findall("sensorT"):
                        id_sensorT = sensorT_elem.get("id")
                        campo_obj.matriz_cultivo.agregar_sensor(id_sensorT)

                # Llena valores del XML
                if sensores_suelo is not None:
                    for sensorS_elem in sensores_suelo.findall("sensorS"):
                        id_sensorS = sensorS_elem.get("id")
                        for frecuencia_elem in sensorS_elem.findall("frecuencia"):
                            id_estacion = frecuencia_elem.get("idEstacion")
                            frecuencia = frecuencia_elem.text
                            campo_obj.matriz_suelo.agregar_valor(id_estacion, id_sensorS, frecuencia)

                if sensores_cultivo is not None:
                    for sensorT_elem in sensores_cultivo.findall("sensorT"):
                        id_sensorT = sensorT_elem.get("id")
                        for frecuencia_elem in sensorT_elem.findall("frecuencia"):
                            id_estacion = frecuencia_elem.get("idEstacion")
                            frecuencia = frecuencia_elem.text
                            campo_obj.matriz_cultivo.agregar_valor(id_estacion, id_sensorT, frecuencia)

                # Completa con ceros si falta algún dato
                campo_obj.matriz_suelo.completar_ceros()
                campo_obj.matriz_cultivo.completar_ceros()

            self.cargado = True
            print("Archivo cargado y procesado correctamente.")
        except Exception as e:
            print("Error al procesar archivo:", e)

    def imprimir_todo(self):
        temp = self.campos.primero
        while temp is not None:
            campo_obj = temp.dato
            print("\n===== Campo", campo_obj.id, "-", campo_obj.nombre, "=====")
            print("-- MATRIZ DE SUELO --")
            self.imprimir_matriz(campo_obj.matriz_suelo)
            print("-- MATRIZ DE CULTIVO --")
            self.imprimir_matriz(campo_obj.matriz_cultivo)
            temp = temp.siguiente

    def imprimir_matriz(self, matriz):
        # Imprime encabezados de sensores
        print("      ", end="")
        temp_sens = matriz.sensores.primero
        while temp_sens is not None:
            print("  ", str(temp_sens.dato), end="")
            temp_sens = temp_sens.siguiente
        print()
        # Imprime filas (estaciones)
        temp_est = matriz.estaciones.primero
        while temp_est is not None:
            print(" ", str(temp_est.dato), end=":")
            nodo_fila = matriz.filas.buscar(temp_est.dato)
            temp_sens = matriz.sensores.primero
            while temp_sens is not None:
                celda = None
                if nodo_fila is not None:
                    celda_nodo = nodo_fila.fila.buscar(temp_sens.dato, "idSensor")
                    if celda_nodo is not None:
                        celda = celda_nodo.dato
                if celda is not None:
                    print("  ", str(celda.frecuencia), end="")
                else:
                    print("  0", end="")
                temp_sens = temp_sens.siguiente
            print()
            temp_est = temp_est.siguiente

    def obtener_campo(self, id_campo):
        temp = self.campos.primero
        while temp is not None:
            if temp.dato.id == id_campo:
                return temp.dato
            temp = temp.siguiente
        return None

    def graficar_matriz(self, id_campo, tipo="suelo"):
        campo = self.obtener_campo(id_campo)
        if campo is None:
            print("Campo no encontrado")
            return
        carpeta = "Salidas"
        if tipo == "suelo":
            campo.matriz_suelo.graficar(carpeta + "/GraficaSuelo_" + str(id_campo) + ".dot",
                                       carpeta + "/GraficaSuelo_" + str(id_campo) + ".png")
        else:
            campo.matriz_cultivo.graficar(carpeta + "/GraficaCultivo_" + str(id_campo) + ".dot",
                                          carpeta + "/GraficaCultivo_" + str(id_campo) + ".png")