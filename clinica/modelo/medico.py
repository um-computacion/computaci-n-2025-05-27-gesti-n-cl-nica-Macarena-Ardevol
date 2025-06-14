from clinica.modelo.especialidad import Especialidad

class Medico:
    def __init__(self, matricula, nombre, apellido, especialidad):
        if not isinstance(matricula, str) or not matricula.isdigit():
            raise ValueError("La matrícula debe ser un string numérico.")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser un string no vacío.")
        if not isinstance(apellido, str) or not apellido.strip():
            raise ValueError("El apellido debe ser un string no vacío.")
        if not isinstance(especialidad, Especialidad):
            raise TypeError("La especialidad debe ser una instancia de la clase Especialidad.")

        self.matricula = matricula
        self.nombre = nombre
        self.apellido = apellido
        self.especialidades = [especialidad] 

    def agregar_especialidad(self, nueva_especialidad):
        if not isinstance(nueva_especialidad, Especialidad):
            raise TypeError("La especialidad debe ser una instancia de la clase Especialidad.")
        if nueva_especialidad not in self.especialidades:
            self.especialidades.append(nueva_especialidad)

    def __str__(self):
        especialidades_str = ", ".join([esp.nombre for esp in self.especialidades])
        return f"Dr. {self.nombre} {self.apellido} (Matrícula: {self.matricula}) - Especialidades: {especialidades_str}"
