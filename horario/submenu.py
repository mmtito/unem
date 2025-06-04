from horario.metodos import generar_horario, eliminar_horario, ver_horario 
class SubmenuH:    
    @staticmethod
    def submenu():
        while True:
            print("\n=============================================")
            print("          Submenú de Matriculas             ")
            print("1. Generar Horario")
            print("2. Ver Horario")
            print("3. Eliminar Horario")
            print("4. Volver al Menú Principal")
            print("=============================================")

            opcion = input("¿Qué necesitas hacer?: ")

            if opcion == "1":
                generar_horario()
            elif opcion == "2":
                ver_horario()
            elif opcion == "3":
                eliminar_horario()
            elif opcion == "4":
                print("Volviendo al menú principal...\n")
                break
            else:
                print("La opción no existe, intenta nuevamente.")
