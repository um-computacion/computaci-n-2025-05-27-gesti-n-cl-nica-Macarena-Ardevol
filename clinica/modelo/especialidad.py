class Especialidad:
    def __init__(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre de la especialidad debe ser un string no vacío.")
        self.nombre = nombre

    def __str__(self):
        return self.nombre
