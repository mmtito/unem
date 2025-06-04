from unemiAdmin import Asignatura
from  docente.metodos import lista_docentes

lista_asignaturas =  []

def agregar_asignatura():
    
    print("\n--- Agregar Nueva Asignatura ---")
    nombre_asig = input("Nombre de la asignatura: ")
    duracion = input("Define la Duración en horas")
    
    if not lista_docentes:
        print(" No hay docentes disponibles.")
        return
    print ("\nDocentes disponibles:")
    for i, doc in enumerate(lista_docentes):
        print(f"{i+1}. {doc.nombre} {doc.apellido} - {doc.especialidad}")
    try:
        indice = int(input("Selecciona el número del docente encargado: ")) -1
        if 0 <= indice < len(lista_docentes):
            docente = lista_docentes[indice]
            nueva_asignatura = Asignatura(nombre_asig, duracion, docente)
            lista_asignaturas.append(nueva_asignatura)
            print(f"Asignatura '{nombre_asig}' agregada con éxito.")
        else :
            print("Seleccion invalida")
    except ValueError:
        print("no válida.")

def listar_asignaturas():
    print("\n--- Lista de asignaturas ---")
    if not lista_asignaturas:
        print("No hay asignaturas registrados.")
    else :
        for i, a in enumerate(lista_asignaturas, 1) :
            print(f"{i}. {a.nombre_asig} | Duración: {a.duracion} | Docente: {a.docente.nombre} {a.docente.apellido}")

def eliminar_asignatura():
    print("\n--- Eliminar asignatura ---")
    nombre_asig = input("Ingrese el nombre de la asignatura que desea eliminar: ")

    for asignatura in lista_asignaturas:
        if asignatura.nombre_asig == nombre_asig:
            lista_asignaturas.remove(asignatura)
            print(f"la asignatura {nombre_asig} fue eliminado con éxito.")
            break
    else:
        print(f"No se encontró ningún asignatura parecida {nombre_asig}.")