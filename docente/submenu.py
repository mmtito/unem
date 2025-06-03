from docente.metodos import agregar_docente, eliminar_docente, listar_docentes
class SubmenuD:
    @staticmethod
    def submenu():
        while True:
            print("\n=============================================")
            print("          Submenú de Docentes            ")
            print("1. Agregar Docentes")
            print("2. Listar Docentes")
            print("3. Eliminar Docentes")
            print("4. Volver al Menú Principal")
            print("=============================================")

            opcion = input("¿Qué necesitas hacer?: ")

            if opcion == "1":
                agregar_docente()
            elif opcion == "2":
                listar_docentes()
            elif opcion == "3":
                eliminar_docente()
            elif opcion == "4":
                print("Volviendo al menú principal...\n")
                break
            else:
                print("La opción no existe, intenta nuevamente.")
