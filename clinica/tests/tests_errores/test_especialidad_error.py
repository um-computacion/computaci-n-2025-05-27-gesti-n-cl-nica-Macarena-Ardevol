import unittest
from clinica.modelo.especialidad import Especialidad

class TestEspecialidadError(unittest.TestCase):

    def test_nombre_none(self):
        with self.assertRaises(ValueError):
            Especialidad(None)

    def test_nombre_entero(self):
        with self.assertRaises(ValueError):
            Especialidad(123)

    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Especialidad("")

    def test_nombre_espacios(self):
        with self.assertRaises(ValueError):
            Especialidad("   ")
