from calificaciones.metodos import agregar_calificacion, listar_calificaciones, eliminar_calificacion
class SubmenuC:
    @staticmethod
    def submenu():
        while True:
            print("\n=============================================")
            print("          Submenú de Calificacions             ")
            print("1. Agregar Calificacions")
            print("2. Listar Calificaciondos")
            print("3. Eliminar Calificaciondos")
            print("4. Volver al Menú Principal")
            print("=============================================")

            opcion = input("¿Qué necesitas hacer?: ")

            if opcion == "1":
                agregar_calificacion()
            elif opcion == "2":
                listar_calificaciones()
            elif opcion == "3":
                eliminar_calificacion()
            elif opcion == "4":
                print("Volviendo al menú principal...\n")
                break
            else:
                print("La opción no existe, intenta nuevamente.")
