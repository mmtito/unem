class Usuario:
    def __init__(self, id_usuario, nombre, apellido):
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._apellido = apellido

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, valor):
        self._id_usuario = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        self._apellido = valor


class Estudiante(Usuario):
    def __init__(self, id_usuario, nombre, apellido, jornada):
        super().__init__(id_usuario, nombre, apellido)
        self._jornada = jornada

    @property
    def jornada(self):
        return self._jornada

    @jornada.setter
    def jornada(self, valor):
        self._jornada = valor


class Docente(Usuario):
    def __init__(self, id_usuario, nombre, apellido, especialidad):
        super().__init__(id_usuario, nombre, apellido)
        self._especialidad = especialidad

    @property
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, valor):
        self._especialidad = valor


class Asignatura:
    def __init__(self, nombre_asig, duracion, docente):
        self._nombre_asig = nombre_asig
        self._duracion = duracion
        self._docente = docente

    @property
    def nombre_asig(self):
        return self._nombre_asig

    @nombre_asig.setter
    def nombre_asig(self, valor):
        self._nombre_asig = valor

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, valor):
        self._duracion = valor

    @property
    def docente(self):
        return self._docente

    @docente.setter
    def docente(self, valor):
        self._docente = valor


class Matricula:
    def __init__(self, estudiante, asignaturas, fecha):
        self._estudiante = estudiante
        self._asignaturas = asignaturas
        self._fecha = fecha

    @property
    def estudiante(self):
        return self._estudiante

    @estudiante.setter
    def estudiante(self, valor):
        self._estudiante = valor

    @property
    def asignaturas(self):
        return self._asignaturas

    @asignaturas.setter
    def asignaturas(self, valor):
        self._asignaturas = valor

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        self._fecha = valor


class Calificacion:
    def __init__(self, estudiante, asignatura, nota):
        self._estudiante = estudiante
        self._asignatura = asignatura
        self._nota = nota

    @property
    def estudiante(self):
        return self._estudiante

    @estudiante.setter
    def estudiante(self, valor):
        self._estudiante = valor

    @property
    def asignatura(self):
        return self._asignatura

    @asignatura.setter
    def asignatura(self, valor):
        self._asignatura = valor

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        self._nota = valor


class Horario:
    def __init__(self, asignatura, dia, hora_inicio, hora_fin):
        self._asignatura = asignatura
        self._dia = dia
        self._hora_inicio = hora_inicio
        self._hora_fin = hora_fin

    @property
    def asignatura(self):
        return self._asignatura

    @asignatura.setter
    def asignatura(self, valor):
        self._asignatura = valor

    @property
    def dia(self):
        return self._dia

    @dia.setter
    def dia(self, valor):
        self._dia = valor

    @property
    def hora_inicio(self):
        return self._hora_inicio

    @hora_inicio.setter
    def hora_inicio(self, valor):
        self._hora_inicio = valor

    @property
    def hora_fin(self):
        return self._hora_fin

    @hora_fin.setter
    def hora_fin(self, valor):
        self._hora_fin = valor
