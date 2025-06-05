from unemiAdmin import Docente

lista_docentes = []

def agregar_docente():
    print("\n--- Agregar Docente ---")
    id_usuario = input("Cédula (10 dígitos numéricos): ").strip()
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    especialidad = input("Especialidad (Informática/Matemática/Base de datos): ").strip()

    # Validar campos vacíos
    if not id_usuario or not nombre or not apellido or not especialidad:
        print("Error: Todos los campos son obligatorios.")
        return

    # Validar cédula
    if not id_usuario.isdigit() or len(id_usuario) != 10:
        print("Error: La cédula debe contener exactamente 10 dígitos numéricos.")
        return

    # Verificar si la cédula ya está registrada
    for docente in lista_docentes:
        if docente.id_usuario == id_usuario:
            print(f"Error: Ya existe un docente registrado con la cédula {id_usuario}.")
            return

    # Validar que nombre y apellido no contengan números
    if not nombre.replace(" ", "").isalpha() or not apellido.replace(" ", "").isalpha():
        print("Error: El nombre y el apellido no deben contener números ni caracteres especiales.")
        return

    # Validar especialidad (ignorando mayúsculas y tildes)
    especialidades_validas = ['informatica', 'matematica', 'base de datos']
    if especialidad.lower() not in especialidades_validas:
        print("Error: Especialidad inválida. Debe ser Informática, Matemática o Base de datos.")
        return

    # Capitalizar correctamente la especialidad
    especialidad = especialidad.capitalize() if especialidad.lower() != 'base de datos' else 'Base de datos'

    docente = Docente(id_usuario, nombre, apellido, especialidad)
    lista_docentes.append(docente)
    print(f"\nDocente {nombre} {apellido} agregado con éxito.")

def listar_docentes():
    print("\n--- Lista de Docentes ---")
    if not lista_docentes:
        print("No hay docentes registrados.")
    else:
        for docente in lista_docentes:
            print(f"Cedula: {docente.id_usuario} | Nombre: {docente.nombre} {docente.apellido} | Especialidad: {docente.especialidad}")

def eliminar_docente():
    print("\n--- Eliminar Docente ---")
    id_usuario = input("Ingrese la cédula del docente que desea eliminar: ").strip()

    if not id_usuario or not id_usuario.isdigit() or len(id_usuario) != 10:
        print("Error: Debe ingresar una cédula válida de 10 dígitos.")
        return

    for docente in lista_docentes:
        if docente.id_usuario == id_usuario:
            lista_docentes.remove(docente)
            print(f"Docente con cédula {id_usuario} eliminado con éxito.")
            break
    else:
        print(f"No se encontró ningún docente con cédula {id_usuario}.")
