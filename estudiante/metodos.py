from unemiAdmin import Estudiante

lista_estudiantes = []

def agregar_estudiante():
    print("\n--- Agregar Estudiante ---")
    
    id_usuario = input("Cédula (10 dígitos numéricos): ").strip()
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    jornada = input("Jornada (mañana/tarde/noche): ").strip().lower()

    # Validación de campos vacíos
    if not id_usuario or not nombre or not apellido or not jornada:
        print("Error: Ningún campo debe estar vacío.")
        return

    # Validación de cédula
    if not id_usuario.isdigit() or len(id_usuario) != 10:
        print("Error: La cédula debe contener exactamente 10 dígitos numéricos.")
        return

    # Validar duplicidad de cédula
    for est in lista_estudiantes:
        if est.id_usuario == id_usuario:
            print(f"Error: Ya existe un estudiante con la cédula {id_usuario}.")
            return

    # Validación de nombre y apellido (sin números ni símbolos)
    if not nombre.replace(" ", "").isalpha() or not apellido.replace(" ", "").isalpha():
        print("Error: El nombre y el apellido no deben contener números ni caracteres especiales.")
        return

    # Validación de jornada
    if jornada not in ['mañana', 'tarde', 'noche']:
        print("Error: Jornada inválida. Debe ser 'mañana', 'tarde' o 'noche'.")
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
            print(f"Cédula: {est.id_usuario} | Nombre: {est.nombre} {est.apellido} | Jornada: {est.jornada.capitalize()}")

def eliminar_estudiante():
    print("\n--- Eliminar Estudiante ---")
    id_usuario = input("Ingrese la cédula del estudiante que desea eliminar: ").strip()

    if not id_usuario or not id_usuario.isdigit() or len(id_usuario) != 10:
        print("Error: Debe ingresar una cédula válida de 10 dígitos.")
        return

    for estudiante in lista_estudiantes:
        if estudiante.id_usuario == id_usuario:
            lista_estudiantes.remove(estudiante)
            print(f"Estudiante con cédula {id_usuario} eliminado con éxito.")
            break
    else:
        print(f"No se encontró ningún estudiante con cédula {id_usuario}.")
