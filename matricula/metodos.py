from unemiAdmin import Matricula
from estudiante.metodos import lista_estudiantes
from asignatura.metodos import lista_asignaturas

lista_matriculas = []

def agregar_matricula():
    print("\n--- Agregar Matrícula ---")

    if not lista_estudiantes:
        print("No hay estudiantes disponibles.")
        return
    if not lista_asignaturas:
        print("No hay asignaturas disponibles.")
        return

    print("\nEstudiantes disponibles:")
    for i, est in enumerate(lista_estudiantes):
        print(f"{i+1}. {est.nombre} {est.apellido} - ID: {est.id_usuario}")

    try:
        indice_est = int(input("Selecciona el número del estudiante a matricular: ")) - 1
        if not (0 <= indice_est < len(lista_estudiantes)):
            print("Selección inválida de estudiante.")
            return
        estudiante = lista_estudiantes[indice_est]
    except ValueError:
        print("Entrada inválida.")
        return

    print("\nAsignaturas disponibles:")
    for i, asig in enumerate(lista_asignaturas):
        print(f"{i+1}. {asig.nombre_asig} - Docente: {asig.docente.nombre} {asig.docente.apellido}")

    indices_asignaturas = input("Selecciona los números de las asignaturas separados por comas (ej: 1,2): ")
    try:
        seleccion = [int(i.strip()) - 1 for i in indices_asignaturas.split(',')]
        asignaturas_seleccionadas = [lista_asignaturas[i] for i in seleccion if 0 <= i < len(lista_asignaturas)]

        if not asignaturas_seleccionadas:
            print("No se seleccionaron asignaturas válidas.")
            return

    except ValueError:
        print("Selección inválida.")
        return

    dia_matriculacion = input("Fecha de matrícula (AAAA-MM-DD): ")

    nueva_matricula = Matricula(estudiante, asignaturas_seleccionadas, dia_matriculacion)
    lista_matriculas.append(nueva_matricula)
    print(" Matrícula registrada con éxito.")

def listar_matriculas():
    print("\n--- Lista de Matrículas ---")
    if not lista_matriculas:
        print("No hay matrículas registradas.")
        return

    for i, mat in enumerate(lista_matriculas, 1):
        estudiante = mat.estudiante
        asignaturas = mat.asignaturas
        fecha = mat.fecha

        print(f"\n📘 Matrícula #{i}")
        print(f"Estudiante: {estudiante.nombre} {estudiante.apellido} (ID: {estudiante.id_usuario})")
        print(f"Fecha de Matrícula: {fecha}")
        print("Asignaturas:")
        for asig in asignaturas:
            print(f"  - {asig.nombre_asig} (Docente: {asig.docente.nombre} {asig.docente.apellido})")

def eliminar_matricula():
    print("\n--- Eliminar Matrícula ---")
    if not lista_matriculas:
        print("No hay matrículas registradas.")
        return

    for i, mat in enumerate(lista_matriculas, 1):
        est = mat.estudiante
        print(f"{i}. {est.nombre} {est.apellido} (ID: {est.id_usuario})")

    try:
        seleccion = int(input("Selecciona el número de la matrícula a eliminar: ")) - 1
        if 0 <= seleccion < len(lista_matriculas):
            eliminado = lista_matriculas.pop(seleccion)
            print(f" Matrícula del estudiante {eliminado.estudiante.nombre} {eliminado.estudiante.apellido} eliminada con éxito.")
        else:
            print("Selección inválida.")
    except ValueError:
        print("Entrada no válida. Debes ingresar un número.")
