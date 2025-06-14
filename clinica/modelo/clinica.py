from clinica.modelo.paciente import Paciente
from clinica.modelo.medico import Medico
from clinica.modelo.turno import Turno
from clinica.modelo.especialidad import Especialidad
from clinica.modelo.receta import Receta
from clinica.modelo.historia_clinica import HistoriaClinica  

class Clinica:
    def __init__(self, nombre="Mi Clínica"):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre de la clínica debe ser un string no vacío.")
        self.nombre = nombre
        self.pacientes = []
        self.medicos = []
        self.turnos = []
        self.recetas = []
        self.historias_clinicas = {}  

    def agregar_paciente(self, paciente):
        if not isinstance(paciente, Paciente):
            raise TypeError("El objeto debe ser una instancia de Paciente.")
        self.pacientes.append(paciente)
        self.historias_clinicas[paciente.dni] = HistoriaClinica(paciente)  

    def agregar_medico(self, medico):
        if not isinstance(medico, Medico):
            raise TypeError("El objeto debe ser una instancia de Medico.")
        self.medicos.append(medico)

    def buscar_paciente_por_dni(self, dni):
        for paciente in self.pacientes:
            if paciente.dni == dni:
                return paciente
        return None

    def buscar_medico_por_matricula(self, matricula):
        for medico in self.medicos:
            if medico.matricula == matricula:
                return medico
        return None

    def agendar_turno(self, turno):
        if not isinstance(turno, Turno):
            raise TypeError("El objeto debe ser una instancia de Turno.")
        self.turnos.append(turno)
        if turno.paciente.dni in self.historias_clinicas:
            self.historias_clinicas[turno.paciente.dni].agregar_turno(turno)

    def agregar_especialidad_a_medico(self, matricula, especialidad):
        medico = self.buscar_medico_por_matricula(matricula)
        if not medico:
            raise ValueError(f"No se encontró médico con matrícula {matricula}")
        medico.agregar_especialidad(especialidad)

    def emitir_receta(self, receta):
        if not isinstance(receta, Receta):
            raise TypeError("El objeto debe ser una instancia de Receta.")
        self.recetas.append(receta)
        if receta.paciente.dni in self.historias_clinicas:
            self.historias_clinicas[receta.paciente.dni].agregar_receta(receta)

    def obtener_historia_clinica(self, dni_paciente):
        return self.historias_clinicas.get(dni_paciente)

    def __str__(self):
        return f"Clínica {self.nombre} con {len(self.pacientes)} pacientes y {len(self.medicos)} médicos."
