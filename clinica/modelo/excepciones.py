class PacienteNoEncontrado(Exception):
    def __init__(self, dni):
        super().__init__(f"No se encontró un paciente con DNI {dni}.")

class MedicoNoDisponible(Exception):
    def __init__(self, nombre):
        super().__init__(f"El médico {nombre} no está disponible para ese turno.")

class TurnoOcupado(Exception):
    def __init__(self, fecha_hora):
        super().__init__(f"Ya existe un turno reservado para la fecha y hora: {fecha_hora}.")

class EspecialidadNoValida(Exception):
    def __init__(self, especialidad):
        super().__init__(f"La especialidad '{especialidad}' no es válida.")
