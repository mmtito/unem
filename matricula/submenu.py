from matricula.metodos import agregar_matricula, listar_matriculas, eliminar_matricula
class SubmenuM:
    @staticmethod
    def submenu():
        while True:
            print("\n=============================================")
            print("          Submenú de Matriculas             ")
            print("1. Agregar Matriculas")
            print("2. Listar Matriculados")
            print("3. Eliminar Matriculados")
            print("4. Volver al Menú Principal")
            print("=============================================")

            opcion = input("¿Qué necesitas hacer?: ")

            if opcion == "1":
                agregar_matricula()
            elif opcion == "2":
                listar_matriculas()
            elif opcion == "3":
                eliminar_matricula()
            elif opcion == "4":
                print("Volviendo al menú principal...\n")
                break
            else:
                print("La opción no existe, intenta nuevamente.")
