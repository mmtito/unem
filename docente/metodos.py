from unemiAdmin import Docente

lista_docentes = []

def agregar_docente():
    print("\n--- Agregar Docente ---")
    id_usuario = input("Cédula: ").strip()
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    especialidad = input("Especialidad (Informática/Matemática/Base de datos): ").strip()

    if not id_usuario or not nombre or not apellido or not especialidad:
        print("Todos los campos son obligatorios.")
        return

    docente = Docente(id_usuario, nombre, apellido, especialidad)
    lista_docentes.append(docente)
    print(f"\nDocente {nombre} {apellido} agregado con éxito.")

def listar_docentes():
    print("\n--- Lista de Docentes ---")
    if not lista_docentes:
        print("No hay docentes registrados.")
    else:
        for docente in lista_docentes:
            print(f"ID: {docente.id_usuario} | Nombre: {docente.nombre} {docente.apellido} | Especialidad: {docente.especialidad}")

def eliminar_docente():
    print("\n--- Eliminar Docente ---")
    id_usuario = input("Ingrese la cédula del docente que desea eliminar: ").strip()

    for docente in lista_docentes:
        if docente.id_usuario == id_usuario:
            lista_docentes.remove(docente)
            print(f"Docente con cédula {id_usuario} eliminado con éxito.")
            break
    else:
        print(f"No se encontró ningún docente con cédula {id_usuario}.")
