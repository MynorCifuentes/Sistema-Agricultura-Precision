class Main:
    def __init__(self):
        pass  

    def menu_principal(self):
        print("\n Bienvenido al menú principal del Gestor para la Agricultura de Precisión")
        print("1] Cargar Archivo")
        print("2] Procesar Archivo")
        print("3] Escribir Archivo de Salida")
        print("4] Mostrar datos del Estudiante")
        print("5] Generar Gráfica")
        print("6] Salir")

    
    def menu_cargar_archivo(self):
        print("\n Cargar Archivo")
        print("1] Ingrese la ruta del archivo a cargar:")
        print("2] Regresar al menú principal")


    def menu_archivo_salida(self):
        print("\n Archivo de Salida")
        print("1] Ingrese la ruta donde desea guardar el archivo")
        print("2] Ingrese el nombre con el que le quiere guardar el archivo")

    def procesar_archivo(self):
        pass

    def mostrar_datos(self):
        pass

    def generar_grafica(self):
        pass


def main():
    gestor = Main()
    gestor.menu_principal()

    while True:
        opcion = input("Ingrese una opcion ")
        if opcion == '1':
            gestor.menu_cargar_archivo()
        elif opcion == '2':
            gestor.procesar_archivo()
        elif opcion == '3':
            gestor.menu_archivo_salida()
        elif opcion == '4':
            gestor.mostrar_datos()
        elif opcion == '5':
            gestor.generar_grafica()
        elif opcion == '6':
            print("Gracias por utilizar el Gestor")
            break

if __name__ == "__main__":
    main()