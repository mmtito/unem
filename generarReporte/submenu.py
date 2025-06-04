from generarReporte.metodos import ver_reporte_calificaciones
class SubmenuR:
    @staticmethod
    def submenu():
       while True:
        print("\n=== Submenú de Reportes ===")
        print("1. Ver reporte de calificaciones")
        print("2. Volver al menú principal")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            ver_reporte_calificaciones()
        elif opcion == "2":
            break
        else:
            print("Opción no válida.")