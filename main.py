#from clinica.modelo.paciente import Paciente
#from clinica.modelo.medico import Medico
#from clinica.modelo.especialidad import Especialidad
#from clinica.modelo.turno import Turno
#from datetime import datetime

#if __name__ == "__main__":
#    paciente = Paciente("12345678", "Ana", "López", "2000-01-01")
    
#    especialidad = Especialidad("Clínica médica")
#    medico = Medico("456", "Juan", "Gómez", especialidad)

#    fecha_turno = datetime(2025, 6, 20, 10, 0)
#    turno = Turno(paciente, medico, fecha_turno)

#    print(turno)

from clinica.interfaz.cli import CLI

if __name__ == "__main__":
    interfaz = CLI()
    interfaz.ejecutar()
