class Paciente:
    def __init__(self, dni, nombre, apellido, fecha_nacimiento):
        # Validación DNI: solo dígitos y entre 7 y 8 caracteres
        if not dni.isdigit() or not (7 <= len(dni) <= 8):
            raise ValueError(f"DNI inválido: {dni}")

        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.historia_clinica = None  

    def __str__(self):
        return f"{self.nombre} {self.apellido} (DNI: {self.dni})"

    def asignar_historia_clinica(self, historia_clinica):
        self.historia_clinica = historia_clinica
