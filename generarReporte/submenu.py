from generarReporte.metodos import ver_reporte_calificaciones

class SubmenuR:
    @staticmethod
    def submenu():
        while True:
            print("\n========================================")
            print("           Submenú de Reportes          ")
            print("1. Ver reporte de calificaciones")
            print("2. Volver al menú principal")
            print("========================================")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                ver_reporte_calificaciones()
            elif opcion == "2":
                print("Volviendo al menú principal...\n")
                break
            else:
                print("Opción no válida, intenta de nuevo.")
