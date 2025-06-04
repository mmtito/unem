from calificaciones.metodos import lista_calificaciones

def ver_reporte_calificaciones():
    print("\n--- Reporte General de Calificaciones ---")

    if not lista_calificaciones:
        print("No hay calificaciones registradas.")
        return

    reporte = {}

    for cal in lista_calificaciones:
        estudiante = f"{cal.estudiante.nombre} {cal.estudiante.apellido}"
        asignatura = cal.asignatura.nombre_asig
        nota = cal.nota

        if estudiante not in reporte:
            reporte[estudiante] = []

        reporte[estudiante].append((asignatura, nota))

    for estudiante, notas in reporte.items():
        print(f"\nEstudiante: {estudiante}")
        for asignatura, nota in notas:
            print(f" - {asignatura}: {nota}")
