from asignatura.metodos import agregar_asignatura, eliminar_asignatura, listar_asignaturas
class SubmenuD:
    @staticmethod
    def submenu():
        while True:
            print("\n=============================================")
            print("          Submenú de Asignaturas            ")
            print("1. Agregar Asignaturas")
            print("2. Listar Asignaturas")
            print("3. Eliminar Asignaturas")
            print("4. Volver al Menú Principal")
            print("=============================================")

            opcion = input("¿Qué necesitas hacer?: ")

            if opcion == "1":
                agregar_asignatura()
            elif opcion == "2":
                listar_asignaturas()
            elif opcion == "3":
                eliminar_asignatura()
            elif opcion == "4":
                print("Volviendo al menú principal...\n")
                break
            else:
                print("La opción no existe, intenta nuevamente.")
