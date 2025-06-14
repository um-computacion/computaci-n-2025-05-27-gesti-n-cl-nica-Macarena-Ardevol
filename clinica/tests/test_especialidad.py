import unittest
from clinica.modelo.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):
    def test_creacion_especialidad(self):
        esp = Especialidad("Cardiología")
        self.assertEqual(esp.nombre, "Cardiología")
