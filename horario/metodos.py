from unemiAdmin import Horario
from matricula.metodos import lista_matriculas

lista_horarios = []

def generar_horario():
    print("\n--- Generar Horario ---")
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
            asignaturas = matricula.asignaturas
            hora_inicio = 7  # Inicio de clases a las 7 AM

            for asignatura in asignaturas:
                try:
                    duracion = int(asignatura.duracion)
                    hora_fin = hora_inicio + duracion
                    dia = input(f"Ingrese el día para {asignatura.nombre_asig} (ej: lunes, martes...): ").capitalize()

                    if dia.lower() not in ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sabado']:
                        print("Día no válido. Se omite la asignatura.")
                        continue

                    horario = Horario(asignatura, dia, hora_inicio, hora_fin)
                    lista_horarios.append(horario)

                    print(f"Horario generado: {asignatura.nombre_asig} | {dia} de {hora_inicio}h a {hora_fin}h")
                    hora_inicio = hora_fin
                except ValueError:
                    print("Duración no válida. Se omite la asignatura.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Entrada no válida.")

def ver_horario():
    print("\n--- Ver Horario ---")
    if not lista_horarios:
        print("No hay horarios registrados.")
        return

    for i, horario in enumerate(lista_horarios, start=1):
        asig = horario.asignatura
        print(f"{i}. Asignatura: {asig.nombre_asig} | Día: {horario.dia} | Hora: {horario.hora_inicio}h - {horario.hora_fin}h")

def eliminar_horario():
    print("\n--- Eliminar Horario ---")
    ver_horario()
    if not lista_horarios:
        return

    try:
        idx = int(input("Selecciona el número del horario a eliminar: ")) - 1
        if 0 <= idx < len(lista_horarios):
            horario = lista_horarios.pop(idx)
            print(f"Horario de {horario.asignatura.nombre_asig} eliminado correctamente.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Entrada no válida.")
