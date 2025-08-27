import xml.etree.ElementTree as ET  # Libreria ElementTree
from Gestor import Gestor
from Estructuras.ListaSimple import ListaSimple 
 
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
        
        newList = ListaSimple()
        newList.agregar("Gabriela",1,1000, 22)
        newList.agregar("Lulu",2,1500, 45)
        newList.agregar("Daniel",3,850, 30)
        newList.agregar("Oto",4, 375, 24)
        
        newList.recorrer()
        newList.graficar("simple1")
        
        
        pass

    def mostrar_datos(self):
        pass

    def generar_grafica(self):
        pass
    
def main():
    gestor = Main()
    gestor.menu_principal()
    miGestor = Gestor()

    while True:
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            miGestor.leer_archivo("/home/mynor/Documents/IPC2_Proyecto1_201318644/Entradas/Entrada1.xml")
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