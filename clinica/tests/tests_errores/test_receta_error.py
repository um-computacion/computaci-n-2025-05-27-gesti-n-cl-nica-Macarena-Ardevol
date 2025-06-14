import unittest
from clinica.modelo.receta import Receta
from clinica.modelo.paciente import Paciente
from clinica.modelo.medico import Medico
from clinica.modelo.especialidad import Especialidad

class TestRecetaError(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("12345678", "Ana","Pérez", "1990-01-01")
        especialidad = Especialidad("Cardiología")
        self.medico = Medico("12345", "Juan", "Gómez", especialidad)

    def test_paciente_invalido(self):
        with self.assertRaises(TypeError):
            Receta("no_es_paciente", self.medico, ["Paracetamol"], "2025-06-12")

    def test_medico_invalido(self):
        with self.assertRaises(TypeError):
            Receta(self.paciente, "no_es_medico", ["Paracetamol"], "2025-06-12")

    def test_medicamentos_invalido(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente, self.medico, "Paracetamol", "2025-06-12")  
        with self.assertRaises(ValueError):
            Receta(self.paciente, self.medico, [], "2025-06-12")  
        with self.assertRaises(ValueError):
            Receta(self.paciente, self.medico, [123, "Ibuprofeno"], "2025-06-12")  

    def test_fecha_invalida(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente, self.medico, ["Paracetamol"], "")
        with self.assertRaises(ValueError):
            Receta(self.paciente, self.medico, ["Paracetamol"], 20250612)  

if __name__ == "__main__":
    unittest.main()
