import unittest
from clinica.modelo.historia_clinica import HistoriaClinica
from clinica.modelo.receta import Receta
from clinica.modelo.paciente import Paciente
from clinica.modelo.medico import Medico
from clinica.modelo.especialidad import Especialidad

class TestHistoriaClinica(unittest.TestCase):
    def test_agregar_receta(self):
        paciente = Paciente("12345678", "Ana", "Pérez", "1990-01-01")
        especialidad = Especialidad("Pediatría")
        medico = Medico("654", "Laura", "Sánchez", especialidad)
        receta = Receta(paciente, medico, ["Ibuprofeno"], "2025-06-12")
        hc = HistoriaClinica(paciente)

        hc.agregar_receta(receta)

        self.assertEqual(len(hc.recetas), 1)
        self.assertEqual(hc.recetas[0].medicamentos[0], "Ibuprofeno")

if __name__ == '__main__':
    unittest.main()

