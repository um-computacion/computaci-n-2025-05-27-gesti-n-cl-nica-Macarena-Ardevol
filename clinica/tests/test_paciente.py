import unittest
from clinica.modelo.paciente import Paciente

class TestPaciente(unittest.TestCase):
    def test_creacion_paciente(self):
        p = Paciente("12345678", "Ana", "Pérez", "12/06/92")
        self.assertEqual(p.dni, "12345678")
        self.assertEqual(p.nombre, "Ana")
        self.assertEqual(p.apellido, "Pérez")
        self.assertEqual(p.fecha_nacimiento, "12/06/92")

if __name__ == "__main__":
    unittest.main()
