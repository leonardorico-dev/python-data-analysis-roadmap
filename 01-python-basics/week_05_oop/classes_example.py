# ==================================================
# Week 4 - OOP in Python
# Topics: Classes, Inheritance, Polymorphism
# ==================================================

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"The {self.brand} {self.model} has started.")
        else:
            print("The car is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"The {self.brand} {self.model} has stopped.")
        else:
            print("The car is already stopped.")

    def description(self):
        return f"Car: {self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_level):
        super().__init__(brand, model)
        self.battery_level = battery_level  # Battery percentage

    def charge_battery(self):
        self.battery_level = 100
        print(f"The {self.brand} battery is fully charged.")

    # Polymorphism (method overriding)
    def description(self):
        return f"Electric Car: {self.brand} {self.model} - Battery: {self.battery_level}%"


if __name__ == "__main__":
    # Create objects
    car1 = Car("Toyota", "Corolla")
    car2 = ElectricCar("Tesla", "Model 3", 80)

    # Use methods
    car1.start()
    car2.start()

    # Polymorphism demonstration
    vehicles = [car1, car2]

    for vehicle in vehicles:
        print(vehicle.description())
