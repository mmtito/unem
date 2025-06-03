class Usuario : 
    def __init__(self, id_usuario, nombre, apellido):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        
class Estudiante(Usuario):
    def __init__(self, id_usuario, nombre, apellido, jornada):
        super().__init__(id_usuario, nombre, apellido)
        self.jornada = jornada
        
class Docente (Usuario):
    def __init__(self, id_usuario, nombre, apellido, especialidad):
        super().__init__(id_usuario, nombre, apellido)
        self.especialidad = especialidad
        
class Asignatura :
    def __init__(self, nombre_asig, duracion, docente):
        self.nombre_asig = nombre_asig 
        self.duracion = duracion
        self.docente = docente # relacion con docente
        
class Matricula :
    def __init__(self ,estudiante, asignaturas, dia_matriculacion):
        self.estudiante =estudiante # relacion con estudiante
        self.asignaturas = asignaturas # relacion con asignatura
        self.dia_matriculacion = dia_matriculacion
        
class Calificacion:
    def __init__(self,  estudiante, asignatura, nota):
        self.estudiante = estudiante  # relacion con estudiante
        self.asignatura = asignatura  # relacion con asignatura
        self.nota = nota
        
class Horario:
    def __init__(self, asignatura, dia, hora_inicio, hora_fin):
        self.asignatura = asignatura              # relacion con asignatura
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        
