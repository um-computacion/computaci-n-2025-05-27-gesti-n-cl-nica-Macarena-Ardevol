import unittest
from clinica.modelo.medico import Medico
from clinica.modelo.especialidad import Especialidad  

class TestMedico(unittest.TestCase):
    def test_creacion_medico(self):
        especialidad = Especialidad("Pediatría")  
        medico = Medico("12345", "Juan", "Gómez", especialidad)
        self.assertEqual(medico.matricula, "12345")
        self.assertEqual(medico.nombre, "Juan")
        self.assertEqual(medico.apellido, "Gómez")
        self.assertEqual(medico.especialidades[0].nombre, "Pediatría")


