from unemiAdmin import Asignatura
from docente.metodos import lista_docentes

lista_asignaturas = []

def agregar_asignatura():
    print("\n--- Agregar Nueva Asignatura ---")

    nombre_asig = input("Nombre de la asignatura: ").strip()

    # Validar nombre vacío o con números/símbolos
    if not nombre_asig or not nombre_asig.replace(" ", "").isalpha():
        print("Error: El nombre de la asignatura no debe estar vacío ni contener números o símbolos.")
        return

    while True:
        duracion_str = input("Define la duración en horas (número entero): ").strip()
        if not duracion_str.isdigit():
            print("Por favor ingresa un número entero válido para la duración.")
        else:
            duracion = int(duracion_str)
            if duracion <= 0:
                print("La duración debe ser mayor a cero.")
            else:
                break

    if not lista_docentes:
        print("No hay docentes disponibles para asignar.")
        return

    print("\nDocentes disponibles:")
    for i, doc in enumerate(lista_docentes):
        print(f"{i+1}. {doc.nombre} {doc.apellido} - {doc.especialidad}")

    try:
        indice = int(input("Selecciona el número del docente encargado: ")) - 1
        if 0 <= indice < len(lista_docentes):
            docente = lista_docentes[indice]
            nueva_asignatura = Asignatura(nombre_asig, duracion, docente)
            lista_asignaturas.append(nueva_asignatura)
            print(f"Asignatura '{nombre_asig}' agregada con éxito.")
        else:
            print("Selección inválida. Número fuera de rango.")
    except ValueError:
        print("Entrada no válida. Debes ingresar un número entero.")

def listar_asignaturas():
    print("\n--- Lista de Asignaturas ---")
    if not lista_asignaturas:
        print("No hay asignaturas registradas.")
    else:
        for i, a in enumerate(lista_asignaturas, 1):
            print(f"{i}. Asignatura: {a.nombre_asig} | Duración: {a.duracion} horas | Docente: {a.docente.nombre} {a.docente.apellido}")

def eliminar_asignatura():
    print("\n--- Eliminar asignatura ---")
    nombre_asig = input("Ingrese el nombre de la asignatura que desea eliminar: ")

    for asignatura in lista_asignaturas:
        if asignatura.nombre_asig == nombre_asig:
            lista_asignaturas.remove(asignatura)
            print(f"La asignatura '{nombre_asig}' fue eliminada con éxito.")
            break
    else:
        print(f"No se encontró ninguna asignatura con el nombre '{nombre_asig}'.")
