from unemiAdmin import Estudiante

lista_estudiantes = []

def agregar_estudiante():
    print("\n--- Agregar Estudiante ---")
    id_usuario = input("Cédula: ").strip()
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    jornada = input("Jornada (mañana/tarde/noche): ").strip().lower()

    if not id_usuario or not nombre or not apellido or jornada not in ['mañana', 'tarde', 'noche']:
        print("Datos inválidos. Todos los campos son obligatorios y la jornada debe ser válida.")
        return

    estudiante = Estudiante(id_usuario, nombre, apellido, jornada)
    lista_estudiantes.append(estudiante)

    print(f"\nEstudiante {nombre} {apellido} agregado con éxito.")

def listar_estudiantes():
    print("\n--- Lista de Estudiantes ---")
    if not lista_estudiantes:
        print("No hay estudiantes registrados.")
    else:
        for est in lista_estudiantes:
            print(f"ID: {est.id_usuario} | Nombre: {est.nombre} {est.apellido} | Jornada: {est.jornada.capitalize()}")

def eliminar_estudiante():
    print("\n--- Eliminar Estudiante ---")
    id_usuario = input("Ingrese la cédula del estudiante que desea eliminar: ").strip()

    for estudiante in lista_estudiantes:
        if estudiante.id_usuario == id_usuario:
            lista_estudiantes.remove(estudiante)
            print(f"Estudiante con cédula {id_usuario} eliminado con éxito.")
            break
    else:
        print(f"No se encontró ningún estudiante con cédula {id_usuario}.")
