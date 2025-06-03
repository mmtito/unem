from unemiAdmin import Asignatura

lista_asignaturas =  []

def agregar_asignatura():
    id_usuario = input("Cedula: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    especialidad = input("Especialidad (Informatica/Matematica/Base de datos): ")

    asignatura = Asignatura(id_usuario, nombre, apellido, especialidad)
    
    lista_asignaturas.append(asignatura) 
    
    print(f"\nasignatura {nombre} {apellido} agregado con éxito.")

def listar_asignaturas():
    print("\n--- Lista de asignaturas ---")
    if not lista_asignaturas:
        print("No hay asignaturas registrados.")
    else :
        for i in lista_asignaturas:
            print(f"ID: {i.id_usuario} | Nombre: {i.nombre} {i.apellido} | Jornada: {i.especialidad}")

def eliminar_asignatura():
    print("\n--- Eliminar asignatura ---")
    id_usuario = input("Ingrese el ID del asignatura que desea eliminar: ")

    for asignatura in lista_asignaturas:
        if asignatura.id_usuario == id_usuario:
            lista_asignaturas.remove(asignatura)
            print(f"asignatura con ID {id_usuario} eliminado con éxito.")
            break
    else:
        print(f"No se encontró ningún asignatura con ID {id_usuario}.")