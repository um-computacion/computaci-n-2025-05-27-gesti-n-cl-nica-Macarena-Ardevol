from clinica.modelo.turno import Turno
from clinica.modelo.receta import Receta

class HistoriaClinica:
    def __init__(self, paciente):
        self.paciente = paciente
        self.turnos = []
        self.recetas = []

    def agregar_turno(self, turno):
        if not isinstance(turno, Turno):
            raise TypeError("El turno debe ser una instancia de la clase Turno.")
        self.turnos.append(turno)

    def agregar_receta(self, receta):
        if not isinstance(receta, Receta):
            raise TypeError("La receta debe ser una instancia de la clase Receta.")
        self.recetas.append(receta)

    def __str__(self):
        resultado = f"Historia clínica de {self.paciente.nombre} {self.paciente.apellido}:\n"

        if self.turnos:
            resultado += "\n🗓️ Turnos:\n"
            for turno in self.turnos:
                resultado += f" - {turno}\n"
        else:
            resultado += "\n🗓️ No hay turnos registrados.\n"

        if self.recetas:
            resultado += "\n💊 Recetas:\n"
            for receta in self.recetas:
                resultado += f" - {receta}\n"
        else:
            resultado += "\n💊 No hay recetas registradas.\n"

        return resultado
