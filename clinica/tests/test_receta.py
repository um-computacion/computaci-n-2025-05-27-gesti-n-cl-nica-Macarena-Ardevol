import unittest
from clinica.modelo.receta import Receta
from clinica.modelo.paciente import Paciente
from clinica.modelo.medico import Medico
from clinica.modelo.especialidad import Especialidad

class TestReceta(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("12345678", "Ana","Pérez", "1990-01-01")
        especialidad = Especialidad("Cardiología")
        self.medico = Medico("12345", "Juan", "Gómez", especialidad)

    def test_creacion_receta(self):
        receta = Receta(self.paciente, self.medico, ["Paracetamol", "Ibuprofeno"], "2025-06-12")
        self.assertEqual(receta.paciente.nombre, "Ana")
        self.assertEqual(receta.medico.nombre, "Juan")
        self.assertListEqual(receta.medicamentos, ["Paracetamol", "Ibuprofeno"])
        self.assertEqual(receta.fecha, "2025-06-12")

    def test_str_receta(self):
        receta = Receta(self.paciente, self.medico, ["Paracetamol", "Ibuprofeno"], "2025-06-12")
        esperado = "Receta para Ana por Juan el 2025-06-12: Paracetamol, Ibuprofeno"
        self.assertEqual(str(receta), esperado)

if __name__ == "__main__":
    unittest.main()
