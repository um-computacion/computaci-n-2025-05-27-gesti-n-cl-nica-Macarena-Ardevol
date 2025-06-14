from datetime import datetime
from clinica.modelo.paciente import Paciente
from clinica.modelo.medico import Medico

class Turno:
    def __init__(self, paciente, medico, fecha_hora):
        if not isinstance(paciente, Paciente):
            raise TypeError("El paciente debe ser una instancia de la clase Paciente.")
        if not isinstance(medico, Medico):
            raise TypeError("El médico debe ser una instancia de la clase Medico.")
        if not isinstance(fecha_hora, datetime):
            raise TypeError("La fecha y hora debe ser un objeto datetime.")
        if fecha_hora <= datetime.now():
            raise ValueError("La fecha y hora del turno debe ser posterior al momento actual.")

        self.paciente = paciente
        self.medico = medico
        self.fecha_hora = fecha_hora

    def __str__(self):
        return f"Turno para {self.paciente.nombre} con el Dr. {self.medico.nombre} el {self.fecha_hora.strftime('%Y-%m-%d %H:%M')}"
