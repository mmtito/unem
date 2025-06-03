from unemiAdmin import Estudiante

lista_estudiantes =  []

def agregar_estudiante():
    id_usuario = input("Cedula: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    jornada = input("Jornada (mañana/tarde/noche): ")

    estudiante = Estudiante(id_usuario, nombre, apellido, jornada)
    
    lista_estudiantes.append(estudiante) 
    
    print(f"\nEstudiante {nombre} {apellido} agregado con éxito.")

def listar_estudiantes ():
    print("\n--- Lista de Estudiantes ---")
    if not lista_estudiantes:
        print("No hay estudiantes registrados.")
    else :
        for i in lista_estudiantes:
            print(f"ID: {i.id_usuario} | Nombre: {i.nombre} {i.apellido} | Jornada: {i.jornada}")

def eliminar_estudiante():
    print("\n--- Eliminar Estudiante ---")
    id_usuario = input("Ingrese el ID del estudiante que desea eliminar: ")

    for estudiante in lista_estudiantes:
        if estudiante.id_usuario == id_usuario:
            lista_estudiantes.remove(estudiante)
            print(f"Estudiante con ID {id_usuario} eliminado con éxito.")
            break
    else:
        print(f"No se encontró ningún estudiante con ID {id_usuario}.")