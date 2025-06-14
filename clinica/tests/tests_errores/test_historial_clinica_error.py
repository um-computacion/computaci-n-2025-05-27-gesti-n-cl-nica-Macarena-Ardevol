import unittest
from datetime import datetime
from clinica.modelo.historia_clinica import HistoriaClinica
from clinica.modelo.paciente import Paciente
from clinica.modelo.turno import Turno
from clinica.modelo.receta import Receta
from clinica.modelo.medico import Medico
from clinica.modelo.especialidad import Especialidad

class TestHistoriaClinicaError(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("12345678", "Ana", "Pérez", "1990-01-01")
        self.especialidad = Especialidad("Cardiología")
        self.medico = Medico("1111", "Carlos", "López", self.especialidad)
        self.historia = HistoriaClinica(self.paciente)
        self.turno_valido = Turno(self.paciente, self.medico, datetime(2025, 6, 10, 10, 0))
        self.receta_valida = Receta(self.paciente, self.medico, ["Ibuprofeno"], "2025-06-10")


    def test_agregar_turno_invalido(self):
        with self.assertRaises(TypeError):
            self.historia.agregar_turno("esto no es un turno")

    def test_agregar_receta_invalida(self):
        with self.assertRaises(TypeError):
            self.historia.agregar_receta(1234)

if __name__ == '__main__':
    unittest.main()
