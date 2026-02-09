# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 13:17:41 2026

@author: lstivanello
"""

"""
9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 65 if it isn’t already. 
Make
an electric car with a default battery size, call get_range() once, and then
call get_range() a second time after upgrading the battery. You should see an
increase in the car’s range.

LO FUI HACIENDO CON IA.. IMPOSIBLE COPIAR Y PEGAR DEL LIBRO ... MALA SUERTE
"""

class Car:
    """Una clase simple para representar un auto convencional."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"Este auto tiene {self.odometer_reading} km recorridos.")

    def update_odometer(self, km):
        # Arreglo: usar >= en lugar de &gt;=
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("No podés hacer retroceder el odómetro.")

    def increment_odometer(self, km):
        self.odometer_reading += km


class Battery:
    """Modela un paquete de batería para autos eléctricos."""

    # 👈 Por consigna, la batería por defecto debe ser menor a 65 para que 'upgrade' tenga efecto.
    def __init__(self, battery_size=40):
        self.battery_size = battery_size  # capacidad (kWh)

    def describe_battery(self):
        print(f"Batería de {self.battery_size}-kWh.")

    def get_range(self):
        """
        Devuelve una autonomía aproximada en km según la capacidad.
        (Valores aproximados para ejemplificar el ejercicio.)
        """
        if self.battery_size == 40:
            range_km = 200
        elif self.battery_size == 65:
            range_km = 340
        else:
            # Puedes ampliar este mapping si quieres soportar más tamaños.
            # En caso contrario, estima proporcionalmente:
            # Asumimos ~5.2 km por kWh (340/65 ≈ 5.23).
            range_km = round(self.battery_size * 5.2)

        print(f"Autonomía aproximada: {range_km} km.")

    def upgrade_battery(self):
        """
        Actualiza la batería a 65 kWh si todavía no lo está (según tu enunciado).
        """
        if self.battery_size < 65:
            self.battery_size = 65
            print("La batería fue actualizada a 65 kWh.")
        else:
            print("La batería ya es de 65 kWh o mayor; no es necesario actualizarla.")


class ElectricCar(Car):
    """Representa aspectos específicos de autos eléctricos."""

    def __init__(self, make, model, year, battery_size=None):
        super().__init__(make, model, year)
        # Permite opcionalmente recibir un tamaño; si no, usa el default (40 kWh).
        self.battery = Battery(battery_size if battery_size is not None else 40)


# --- Prueba del ejercicio 9-9 ---

tesla = ElectricCar('Tesla', 'Model X', 2023)  # por defecto batería=40 kWh
tesla.battery.describe_battery()
tesla.battery.get_range()

print("\nActualizando batería...\n")
tesla.battery.upgrade_battery()

tesla.battery.describe_battery()
tesla.battery.get_range()