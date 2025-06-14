import unittest
from datetime import datetime
from clinica.modelo.turno import Turno
from clinica.modelo.paciente import Paciente
from clinica.modelo.medico import Medico
from clinica.modelo.especialidad import Especialidad

class TestTurnoError(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("12345678", "Ana", "Pérez","1990-01-01")
        self.especialidad = Especialidad("Cardiología")
        self.medico = Medico("98765", "Juan", "Pérez", self.especialidad)
        self.fecha_hora = datetime(2025, 6, 15, 10, 30)

    def test_paciente_invalido(self):
        with self.assertRaises(TypeError):
            Turno("no_paciente", self.medico, self.fecha_hora)

    def test_medico_invalido(self):
        with self.assertRaises(TypeError):
            Turno(self.paciente, "no_medico", self.fecha_hora)

    def test_fecha_hora_invalida(self):
        with self.assertRaises(TypeError):
            Turno(self.paciente, self.medico, "2025-06-15 10:30")

if __name__ == '__main__':
    unittest.main()
