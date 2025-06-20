from estudiante.submenu import SubmenuE
from docente.submenu import SubmenuD
from asignatura.submenu import SubmenuA
from matricula.submenu import SubmenuM
from calificaciones.submenu import SubmenuC
from horario.submenu import SubmenuH
from generarReporte.submenu import SubmenuR

def menu():
    print("\n=============================================")
    print("          Sistema de Gestión Académica       ")
    print("=============================================")
    print("1. Estudiantes")
    print("2. Docentes")
    print("3. Asignaturas")
    print("4. Matrícula")
    print("5. Calificaciones")
    print("6. Horarios")
    print("7. Reportes")
    print("8. Salir")
    print("=============================================")

while True:
    menu()
    opcion = input("Escoge una opción: ")

    if opcion == "1":
        SubmenuE.submenu()
    elif opcion == "2":
        SubmenuD.submenu()
    elif opcion == "3":
        SubmenuA.submenu()
    elif opcion == "4":
        SubmenuM.submenu()
    elif opcion == "5":
        SubmenuC.submenu()
    elif opcion == "6":
        SubmenuH.submenu()
    elif opcion == "7":
        SubmenuR.submenu()
    elif opcion == "8":
        print(" Has salido con éxito del sistema. ¡Hasta pronto!")
        break
    else:
        print(" Opción no válida. Intenta nuevamente.")
