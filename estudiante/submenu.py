from estudiante.metodos import agregar_estudiante,listar_estudiantes, eliminar_estudiante
class SubmenuE:
    @staticmethod
    def submenu():
        while True:
            print("\n=============================================")
            print("          Submenú de Estudiantes             ")
            print("1. Agregar Estudiantes")
            print("2. Listar Estudiantes")
            print("3. Eliminar Estudiantes")
            print("4. Volver al Menú Principal")
            print("=============================================")

            opcion = input("¿Qué necesitas hacer?: ")

            if opcion == "1":
                agregar_estudiante()
            elif opcion == "2":
                listar_estudiantes()
            elif opcion == "3":
                eliminar_estudiante()
            elif opcion == "4":
                print("Volviendo al menú principal...\n")
                break
            else:
                print("La opción no existe, intenta nuevamente.")
