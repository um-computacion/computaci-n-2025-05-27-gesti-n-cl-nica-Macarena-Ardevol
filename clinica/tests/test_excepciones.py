import unittest
from clinica.modelo.excepciones import (
    PacienteNoEncontrado,
    MedicoNoDisponible,
    TurnoOcupado,
    EspecialidadNoValida
)

class TestExcepciones(unittest.TestCase):
    def test_paciente_no_encontrado(self):
        dni = "12345678"
        with self.assertRaises(PacienteNoEncontrado) as cm:
            raise PacienteNoEncontrado(dni)
        self.assertEqual(str(cm.exception), f"No se encontró un paciente con DNI {dni}.")

    def test_medico_no_disponible(self):
        nombre = "Dr. Pérez"
        with self.assertRaises(MedicoNoDisponible) as cm:
            raise MedicoNoDisponible(nombre)
        self.assertEqual(str(cm.exception), f"El médico {nombre} no está disponible para ese turno.")

    def test_turno_ocupado(self):
        fecha_hora = "2025-06-15 10:00"
        with self.assertRaises(TurnoOcupado) as cm:
            raise TurnoOcupado(fecha_hora)
        self.assertEqual(str(cm.exception), f"Ya existe un turno reservado para la fecha y hora: {fecha_hora}.")

    def test_especialidad_no_valida(self):
        especialidad = "Fantasía"
        with self.assertRaises(EspecialidadNoValida) as cm:
            raise EspecialidadNoValida(especialidad)
        self.assertEqual(str(cm.exception), f"La especialidad '{especialidad}' no es válida.")

if __name__ == "__main__":
    unittest.main()
