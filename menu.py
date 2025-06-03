from estudiante.submenu import SubmenuE
from docente.submenu import SubmenuD


def menu():
    print("\n=============================================")
    print("          Sistema de Gestión Académica       ")
    print("1. Estudiantes")
    print("2. Docentes")
    print("3. Asignaturas")
    print("4. Matrícula")
    print("5. Calificación")
    print("6. Horario")
    print("7. Salir")
    print("=============================================")

while True:
    menu()
    opcion = input("Escoge una opción: ")

    if opcion == "1":
        SubmenuE.submenu()
    elif opcion == "2":
        SubmenuD.submenu()
    elif opcion == "3":
        print("Estás en la opción: Asignaturas")
    elif opcion == "4":
        print("Estás en la opción: Matrícula")
    elif opcion == "5":
        print("Estás en la opción: Calificación")
    elif opcion == "6":
        print("Estás en la opción: Horario")
    elif opcion == "7":
        print("Has salido con éxito...")
        break
    else:
        print("El dígito no existe en la lista, intenta nuevamente.")
