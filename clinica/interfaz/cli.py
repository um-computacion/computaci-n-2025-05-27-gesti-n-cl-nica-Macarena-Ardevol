from clinica.modelo.clinica import Clinica
from clinica.modelo.paciente import Paciente
from clinica.modelo.medico import Medico
from clinica.modelo.especialidad import Especialidad
from clinica.modelo.turno import Turno
from clinica.modelo.receta import Receta
from datetime import datetime

class CLI:
    def __init__(self):
        self.clinica = Clinica()

    def mostrar_menu(self):
        print("\n--- Menú Clínica ---")
        print("1) Agregar paciente")
        print("2) Agregar médico")
        print("3) Agendar turno")
        print("4) Agregar especialidad")
        print("5) Emitir receta")
        print("6) Ver historia clínica")
        print("7) Ver todos los turnos")
        print("8) Ver todos los pacientes")
        print("9) Ver todos los médicos")
        print("0) Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self.agregar_paciente()
            elif opcion == "2":
                self.agregar_medico()
            elif opcion == "3":
                self.agendar_turno()
            elif opcion == "4":
                self.agregar_especialidad_a_medico()
            elif opcion == "5":
                self.emitir_receta()
            elif opcion == "6":
                self.ver_historia_clinica()
            elif opcion == "7":
                self.ver_todos_los_turnos()
            elif opcion == "8":
                self.ver_todos_los_pacientes()
            elif opcion == "9":
                self.ver_todos_los_medicos()
            elif opcion == "0":
                print(" Saliendo del sistema. ¡Hasta luego!")
                break
            else:
                print(" Opción inválida. Intente nuevamente.")

    def agregar_paciente(self):
        try:
            dni = input("Ingrese DNI: ").strip()
            nombre = input("Ingrese nombre: ").strip()
            apellido = input("Ingrese apellido: ").strip()
            fecha_nac = input("Ingrese fecha de nacimiento (YYYY-MM-DD): ").strip()
            paciente = Paciente(dni, nombre, apellido, fecha_nac)
            self.clinica.agregar_paciente(paciente)
            print(f" Paciente {nombre} {apellido} agregado correctamente.")
        except Exception as e:
            print(f" Error al agregar paciente: {e}")

    def agregar_medico(self):
        try:
            matricula = input("Ingrese matrícula del médico: ").strip()
            nombre = input("Ingrese nombre del médico: ").strip()
            apellido = input("Ingrese apellido del médico: ").strip()

            nombre_esp = input("Ingrese nombre de la especialidad: ").strip()
            especialidad = Especialidad(nombre_esp)

            medico = Medico(matricula, nombre, apellido, especialidad)
            self.clinica.agregar_medico(medico)
            print(f" Médico {nombre} {apellido} agregado correctamente.")
        except Exception as e:
            print(f" Error al agregar médico: {e}")

    def agendar_turno(self):
        try:
            dni_paciente = input("Ingrese DNI del paciente: ").strip()
            paciente = self.clinica.buscar_paciente_por_dni(dni_paciente)
            if not paciente:
                print(f" No se encontró paciente con DNI {dni_paciente}")
                return

            matricula_medico = input("Ingrese matrícula del médico: ").strip()
            medico = self.clinica.buscar_medico_por_matricula(matricula_medico)
            if not medico:
                print(f" No se encontró médico con matrícula {matricula_medico}")
                return

            fecha_str = input("Ingrese fecha y hora del turno (YYYY-MM-DD HH:MM): ").strip()
            fecha_turno = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")

            turno = Turno(paciente, medico, fecha_turno)
            self.clinica.agendar_turno(turno)
            print(f" Turno agendado para {paciente.nombre} con Dr. {medico.apellido} el {fecha_turno}")
        except Exception as e:
            print(f" Error al agendar turno: {e}")
    
    def agregar_especialidad_a_medico(self):
        try:
            matricula = input("Ingrese matrícula del médico: ").strip()
            nombre_esp = input("Ingrese nombre de la nueva especialidad: ").strip()
            especialidad = Especialidad(nombre_esp)
            self.clinica.agregar_especialidad_a_medico(matricula, especialidad)
            print(f" Especialidad '{nombre_esp}' agregada correctamente al médico con matrícula {matricula}.")
        except Exception as e:
            print(f" Error al agregar especialidad: {e}")
    
    def emitir_receta(self):
        try:
            dni = input("Ingrese DNI del paciente: ").strip()
            paciente = self.clinica.buscar_paciente_por_dni(dni)
            if not paciente:
                print(f" No se encontró paciente con DNI {dni}")
                return

            matricula = input("Ingrese matrícula del médico: ").strip()
            medico = self.clinica.buscar_medico_por_matricula(matricula)
            if not medico:
                print(f" No se encontró médico con matrícula {matricula}")
                return

            medicamentos_input = input("Ingrese medicamentos separados por coma: ").strip()
            medicamentos = [med.strip() for med in medicamentos_input.split(",") if med.strip()]
            if not medicamentos:
                print(" Debe ingresar al menos un medicamento.")
                return

            fecha = input("Ingrese la fecha de la receta (YYYY-MM-DD): ").strip()

            receta = Receta(paciente, medico, medicamentos, fecha)
            self.clinica.emitir_receta(receta)
            print(f" Receta emitida correctamente:\n{receta}")
        except Exception as e:
            print(f" Error al emitir receta: {e}")
    
    def ver_historia_clinica(self):
        try:
            dni = input("Ingrese DNI del paciente: ").strip()
            historia = self.clinica.obtener_historia_clinica(dni)
            if not historia:
                print(f" No se encontró historia clínica para el paciente con DNI {dni}")
                return
            
            print(f"\n Historia clínica de {historia.paciente.nombre} {historia.paciente.apellido}:\n")

            if historia.turnos:
                print(" Turnos:")
                for turno in historia.turnos:
                    print(f" - {turno}")
            else:
                print(" No hay turnos registrados.")

            if historia.recetas:
                print("\n Recetas:")
                for receta in historia.recetas:
                    print(f" - {receta}")
            else:
                print("\n No hay recetas registradas.")

        except Exception as e:
            print(f" Error al ver historia clínica: {e}")

    def ver_todos_los_turnos(self):
        if not self.clinica.turnos:
            print(" No hay turnos agendados.")
            return
        print("\n Turnos agendados:")
        for turno in self.clinica.turnos:
            print(turno)

    def ver_todos_los_pacientes(self):
        if not self.clinica.pacientes:
            print(" No hay pacientes registrados.")
            return
        print("\n Lista de pacientes:")
        for paciente in self.clinica.pacientes:
            print(paciente)

    def ver_todos_los_medicos(self):
        if not self.clinica.medicos:
            print(" No hay médicos registrados.")
            return
        print("\n Lista de médicos:")
        for medico in self.clinica.medicos:
            print(medico)


