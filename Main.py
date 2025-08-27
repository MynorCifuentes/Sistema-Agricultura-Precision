import xml.etree.ElementTree as ET  # Libreria ElementTree

class Main:
    def __init__(self):
        pass

    def menu_principal(self):
        print("\n---------- GESTOR PARA LA AGRICULTURA DE PRECISIÓN ----------")
        print("  1. Cargar archivo")
        print("  2. Procesar archivo")
        print("  3. Escribir archivo de salida")
        print("  4. Mostrar datos del estudiante")
        print("  5. Generar gráfica")
        print("  6. Salir")
        print("---------------------------------------------------------------")

    def menu_cargar_archivo(self):
        print("\n---------- CARGAR ARCHIVO ----------")
        print("  1. Ingrese la ruta del archivo a cargar")
        print("  2. Regresar al menú principal")
        print("------------------------------------")

    def menu_archivo_salida(self):
        print("\n---------- ARCHIVO DE SALIDA ----------")
        print("  1. Ingrese la ruta donde desea guardar el archivo")
        print("  2. Ingrese el nombre con el que desea guardar el archivo")
        print("----------------------------------------")

    def procesar_archivo(self):
        pass

    def mostrar_datos(self):
        pass

    def generar_grafica(self):
        pass
    
    def leer_archivo(self,ruta_entrada):
        tree = ET.parse(ruta_entrada)
        root = tree.getroot() 
        print(root.tag)#camposAgricolas
        
        for campo_elem in root.findall("campo"):
            id_campo = campo_elem.get("id")
            nombre_campo = campo_elem.get("nombre")
            print("---------------------------------------------------------------")
            print("El id del campo es: ",id_campo, "nombre: ",nombre_campo)
            
            #estacionesBase
            for estaciones_elem in campo_elem.find("estacionesBase").findall("estacion"):
                id_estacion = estaciones_elem.get("id")
                nombre_estacion = estaciones_elem.get("nombre")
                print("El id de la estacion es: ",id_estacion, "nombre: ",nombre_estacion)
            
            #sensoresSuelo
            for sensoresS_elem in campo_elem.find("sensoresSuelo").findall("sensorS"):
                id_sensorS = sensoresS_elem.get("id")
                nombre_sensorS = sensoresS_elem.get("nombre")
                print(" ")
                print("El id del sensor de suelo es: ",id_sensorS, "nombre: ",nombre_sensorS)
                for frecuencia_elem in sensoresS_elem.findall("frecuencia"):
                    id_estacionS = frecuencia_elem.get("idEstacion") 
                    #Frecuencia de las estaciones para los sensores de suelo
                    frecuenciaS = int(sensoresS_elem.find("frecuencia").text)   
                    print("El id de la estacion para el Sensor de suelo: ", id_estacionS, "con una frecuencia de: ",frecuenciaS)
                                
            #sensoresCultivo
            for sensoresT_elem in campo_elem.find("sensoresCultivo").findall("sensorT"):
                id_sensorT = sensoresT_elem.get("id")
                nombre_sensorT = sensoresT_elem.get("nombre")
                print("El id del sensor de cultivo es: ",id_sensorT, "nombre: ",nombre_sensorT)
                for frecuencia_elem in sensoresT_elem.findall("frecuencia"):
                    id_estacionT = frecuencia_elem.get("idEstacion") 
                    #Frecuencia de las estaciones para los sensores de suelo
                    frecuenciaT = int(sensoresS_elem.find("frecuencia").text)   
                    print("El id de la estacion para el Sensor de cultivo: ", id_estacionT, "con una frecuencia de: ",frecuenciaT)



            
        
            

def main():
    gestor = Main()
    gestor.menu_principal()

    while True:
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            gestor.leer_archivo("/home/mynor/Documents/IPC2_Proyecto1_201318644/Entradas/Entrada1.xml")
            # gestor.menu_cargar_archivo()
        elif opcion == '2':
            gestor.procesar_archivo()
        elif opcion == '3':
            gestor.menu_archivo_salida()
        elif opcion == '4':
            gestor.mostrar_datos()
        elif opcion == '5':
            gestor.generar_grafica()
        elif opcion == '6':
            print("\nGracias por utilizar el gestor.")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")
        print()

if __name__ == "__main__":
    main()