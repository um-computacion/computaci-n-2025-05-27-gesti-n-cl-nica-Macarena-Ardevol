import unittest
from clinica.modelo.clinica import Clinica
from clinica.modelo.paciente import Paciente
from clinica.modelo.medico import Medico
from clinica.modelo.especialidad import Especialidad

class TestClinica(unittest.TestCase):
    def test_agregar_paciente_y_medico(self):
        clinica = Clinica("Salud Total")

        paciente = Paciente("12345678", "Juan", "Pérez", "1985-06-15")
        especialidad = Especialidad("Pediatría")
        medico = Medico("98765432", "Laura", "Gómez", especialidad)

        clinica.agregar_paciente(paciente)
        clinica.agregar_medico(medico)

        self.assertEqual(len(clinica.pacientes), 1)
        self.assertEqual(len(clinica.medicos), 1)
        self.assertEqual(clinica.pacientes[0].nombre, "Juan")
        self.assertEqual(clinica.medicos[0].apellido, "Gómez")
