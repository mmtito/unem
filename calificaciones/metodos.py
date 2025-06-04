from unemiAdmin import Calificacion
from matricula.metodos import lista_matriculas

lista_calificaciones = []

def agregar_calificacion():
    print("\n--- Agregar Calificación ---")

    if not lista_matriculas:
        print("No hay matrículas registradas.")
        return

    print("\nEstudiantes matriculados:")
    for i, mat in enumerate(lista_matriculas):
        est = mat.estudiante
        print(f"{i+1}. {est.nombre} {est.apellido}")

    try:
        idx = int(input("Selecciona el número del estudiante: ")) - 1
        if 0 <= idx < len(lista_matriculas):
            matricula = lista_matriculas[idx]
            estudiante = matricula.estudiante
            asignaturas = matricula.asignaturas

            for asig in asignaturas:
                print(f"\nAsignatura: {asig.nombre_asig} (Docente: {asig.docente.nombre} {asig.docente.apellido})")
                try:
                    nota = float(input("Ingresa la nota: "))
                    calificacion = Calificacion(estudiante, asig, nota)
                    lista_calificaciones.append(calificacion)
                    print("Calificación registrada con éxito.")
                except ValueError:
                    print("Nota no válida. Se omite esta asignatura.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Entrada no válida.")

def listar_calificaciones():
    print("\n--- Lista de Calificaciones ---")
    if not lista_calificaciones:
        print("No hay calificaciones registradas.")
    else:
        for i, cal in enumerate(lista_calificaciones, 1):
            print(f"{i}. Estudiante: {cal.estudiante.nombre} {cal.estudiante.apellido} | Asignatura: {cal.asignatura.nombre_asig} | Nota: {cal.nota}")

def eliminar_calificacion():
    print("\n--- Eliminar Calificación ---")
    listar_calificaciones()
    try:
        idx = int(input("Selecciona el número de la calificación a eliminar: ")) - 1
        if 0 <= idx < len(lista_calificaciones):
            cal = lista_calificaciones.pop(idx)
            print(f"Calificación de {cal.estudiante.nombre} en {cal.asignatura.nombre_asig} eliminada.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Entrada no válida.")