import unittest
from clinica.modelo.paciente import Paciente

class TestErrorPaciente(unittest.TestCase):
    def test_dni_invalido_letras(self):
        with self.assertRaises(ValueError) as cm:
            Paciente("12A45678", "Ana", "Pérez", "1990-01-01")
        self.assertEqual(str(cm.exception), "DNI inválido: 12A45678")

    def test_dni_invalido_corto(self):
        with self.assertRaises(ValueError) as cm:
            Paciente("123456", "Ana", "Pérez", "1990-01-01")
        self.assertEqual(str(cm.exception), "DNI inválido: 123456")

    def test_dni_invalido_largo(self):
        with self.assertRaises(ValueError) as cm:
            Paciente("123456789", "Ana", "Pérez", "1990-01-01")
        self.assertEqual(str(cm.exception), "DNI inválido: 123456789")

if __name__ == "__main__":
    unittest.main()
