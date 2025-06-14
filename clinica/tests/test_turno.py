import unittest
from datetime import datetime
from clinica.modelo.turno import Turno
from clinica.modelo.paciente import Paciente
from clinica.modelo.medico import Medico
from clinica.modelo.especialidad import Especialidad

class TestTurno(unittest.TestCase):
    def test_creacion_turno(self):
        paciente = Paciente("12345678", "Ana", "López", "1990-01-01")
        especialidad = Especialidad("Cardiología")
        medico = Medico("456", "Juan", "Gómez", especialidad)
        fecha = datetime(2025, 6, 15, 10, 0)

        turno = Turno(paciente, medico, fecha)

        self.assertEqual(turno.paciente.nombre, "Ana")
        self.assertEqual(turno.medico.nombre, "Juan")
        self.assertEqual(turno.fecha_hora, fecha)

if __name__ == '__main__':
    unittest.main()
