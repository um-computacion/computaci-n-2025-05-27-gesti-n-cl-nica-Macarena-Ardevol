from clinica.modelo.paciente import Paciente
from clinica.modelo.medico import Medico

class Receta:
    def __init__(self, paciente, medico, medicamentos: list, fecha):
        if not isinstance(paciente, Paciente):
            raise TypeError("El paciente debe ser una instancia de la clase Paciente.")
        if not isinstance(medico, Medico):
            raise TypeError("El médico debe ser una instancia de la clase Medico.")
        if not isinstance(medicamentos, list) or not medicamentos or not all(isinstance(med, str) for med in medicamentos):
            raise ValueError("Medicamentos debe ser una lista no vacía de strings.")
        if not isinstance(fecha, str) or not fecha.strip():
            raise ValueError("Fecha debe ser un string no vacío.")

        self.paciente = paciente
        self.medico = medico
        self.medicamentos = medicamentos
        self.fecha = fecha

    def __str__(self):
        meds = ", ".join(self.medicamentos)
        return f"Receta para {self.paciente.nombre} por {self.medico.nombre} el {self.fecha}: {meds}"
