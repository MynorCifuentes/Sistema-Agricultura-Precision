from Gestor import Gestor
import os

class Main:
    def __init__(self):
        self.gestor = Gestor()

    def menu_principal(self):
        print("\n---------- GESTOR PARA LA AGRICULTURA DE PRECISIÓN ----------")
        print("  1. Cargar archivo XML")
        print("  2. Mostrar matrices")
        print("  3. Graficar matriz")
        print("  4. Mostrar datos del estudiante")
        print("  5. Salir")
        print("-------------------------------------------------------------")

    def loop(self):
        while True:
            self.menu_principal()
            opcion = input("Seleccione una opción: ").strip()
            if opcion == '1':
                ruta = input("Ruta del XML (ENTER para Entradas/Entrada1.xml): ").strip()
                if ruta == "":
                    ruta = os.path.join("Entradas", "Entrada1.xml")
                self.gestor.leer_archivo(ruta)
            elif opcion == '2':
                self.gestor.imprimir_todo()
            elif opcion == '3':
                id_campo = input("Ingrese ID del campo (ej: 02): ").strip()
                tipo = input("Tipo de matriz (suelo/cultivo): ").strip().lower()
                self.gestor.graficar_matriz(id_campo, tipo)
            elif opcion == '4':
                print("Mynor Alejandro Cifuentes")
                print("Carné: 201318644")
                print("Curso: IPC2")
                print("https://mynorcifuentes.github.io/")
            elif opcion == '5':
                print("Gracias por utilizar el gestor.")
                break
            else:
                print("Opción inválida.")

if __name__ == "__main__":
    app = Main()
    app.loop()