from unemiAdmin import Docente

lista_docentes =  []

def agregar_docente():
    id_usuario = input("Cedula: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    especialidad = input("Especialidad (Informatica/Matematica/Base de datos): ")

    docente = Docente(id_usuario, nombre, apellido, especialidad)
    
    lista_docentes.append(docente) 
    
    print(f"\ndocente {nombre} {apellido} agregado con éxito.")

def listar_docentes():
    print("\n--- Lista de docentes ---")
    if not lista_docentes:
        print("No hay docentes registrados.")
    else :
        for i in lista_docentes:
            print(f"ID: {i.id_usuario} | Nombre: {i.nombre} {i.apellido} | Jornada: {i.especialidad}")

def eliminar_docente():
    print("\n--- Eliminar docente ---")
    id_usuario = input("Ingrese el ID del docente que desea eliminar: ")

    for docente in lista_docentes:
        if docente.id_usuario == id_usuario:
            lista_docentes.remove(docente)
            print(f"docente con ID {id_usuario} eliminado con éxito.")
            break
    else:
        print(f"No se encontró ningún docente con ID {id_usuario}.")