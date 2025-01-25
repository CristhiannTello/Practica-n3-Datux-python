# Realice un programa que pueda gestionar tickets de buses
# las clases a usar seran buses  , conductores
# 1. Un menu iteractivo con las siguiente opciones: agregar bus , agregar ruta a bus 
# registrar horario a bus, agregar conductor , agregar horario a conductor(*) y asignar bus a conductor(**)
# * consideremos que el horario de los conductores solo es a nivel de horas mas no dias ni fechas
# **validar que no haya conductores en ese horario ya asignados


class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = []  # Lista de horarios asignados al conductor

    def agregar_horario(self, horario):
        if horario not in self.horarios:
            self.horarios.append(horario)
            return True
        return False


class Bus:
    def __init__(self, ruta):
        self.ruta = ruta
        self.conductores_asignados = []  # Lista de conductores asignados al bus
        self.horarios = []  # Lista de horarios del bus

    def asignar_conductor(self, conductor, horario):
        # Verificar si ya existe el horario en este bus
        if horario in self.horarios:
            return False  # Conflicto en este bus

        # Si no hay conflicto, agregar conductor y horario al bus
        self.conductores_asignados.append(conductor)
        self.horarios.append(horario)
        return True


class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self, ruta):
        nuevo_bus = Bus(ruta)
        self.buses.append(nuevo_bus)
        print(f"Bus con ruta '{ruta}' agregado.")

    def agregar_conductor(self, nombre):
        nuevo_conductor = Conductor(nombre)
        self.conductores.append(nuevo_conductor)
        print(f"Conductor '{nombre}' agregado.")

    def horario_disponible(self, nombre_conductor, horario):
        # Verificar si el conductor ya tiene el horario asignado en algún bus
        conductor = next((c for c in self.conductores if c.nombre == nombre_conductor), None)
        if conductor and horario in conductor.horarios:
            return False
        return True

    def asignar_bus_a_conductor(self, ruta, nombre_conductor, horario):
        bus = next((b for b in self.buses if b.ruta == ruta), None)
        conductor = next((c for c in self.conductores if c.nombre == nombre_conductor), None)

        if not bus:
            print(f"No se encontró un bus con la ruta '{ruta}'.")
            return

        if not conductor:
            print(f"No se encontró un conductor con el nombre '{nombre_conductor}'.")
            return

        if not self.horario_disponible(nombre_conductor, horario):
            print(f"El conductor '{nombre_conductor}' ya tiene asignado el horario '{horario}' en otro bus.")
            return

        if bus.asignar_conductor(conductor, horario):
            conductor.agregar_horario(horario)  # Asignar horario al conductor
            print(f"Conductor '{nombre_conductor}' asignado al bus de ruta '{ruta}' en el horario '{horario}'.")
        else:
            print(f"No se pudo asignar al conductor '{nombre_conductor}' en el horario '{horario}'. Conflicto en este bus.")

    def mostrar_buses(self):
        for bus in self.buses:
            print(f"Ruta: {bus.ruta}, Horarios: {bus.horarios}, Conductores: {[c.nombre for c in bus.conductores_asignados]}")

    def mostrar_conductores(self):
        for conductor in self.conductores:
            print(f"Nombre: {conductor.nombre}, Horarios: {conductor.horarios}")


# Menú interactivo
admin = Admin()

while True:
    print("\nOpciones:")
    print("1. Agregar bus")
    print("2. Agregar conductor")
    print("3. Asignar bus a conductor")
    print("4. Mostrar buses")
    print("5. Mostrar conductores")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ruta = input("Ingrese la ruta del bus: ")
        admin.agregar_bus(ruta)

    elif opcion == "2":
        nombre = input("Ingrese el nombre del conductor: ")
        admin.agregar_conductor(nombre)

    elif opcion == "3":
        ruta = input("Ingrese la ruta del bus: ")
        nombre_conductor = input("Ingrese el nombre del conductor: ")
        horario = input("Ingrese el horario (HH:MM): ")
        admin.asignar_bus_a_conductor(ruta, nombre_conductor, horario)

    elif opcion == "4":
        admin.mostrar_buses()

    elif opcion == "5":
        admin.mostrar_conductores()

    elif opcion == "6":
        print("Saliendo del programa.")
        break

    else:
        print("Por favor, intente una opción válida.")
