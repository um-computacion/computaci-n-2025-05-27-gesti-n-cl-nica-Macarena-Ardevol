import unittest
from clinica.modelo.medico import Medico
from clinica.modelo.especialidad import Especialidad

class TestMedicoError(unittest.TestCase):
    def test_matricula_invalida(self):
        with self.assertRaises(ValueError):
            Medico(1234, "Carlos", "Gómez", Especialidad("Pediatría"))  # matrícula no es string

    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Medico("5678", "", "Gómez", Especialidad("Pediatría"))

    def test_apellido_vacio(self):
        with self.assertRaises(ValueError):
            Medico("5678", "Carlos", "   ", Especialidad("Pediatría"))

    def test_especialidad_invalida(self):
        with self.assertRaises(TypeError):
            Medico("1234", "Carlos", "Gómez", "no_es_objeto")

if __name__ == '__main__':
    unittest.main()
