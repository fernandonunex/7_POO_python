import os

class Automobile:

    def __init__(self, model, brand, color, year):
        self.model = model
        self.brand = brand
        self.color = color
        self.year = year
        self._state = 'static'
        self._motor = Motor(cylinders=4)
        self.tires = Tires('city',20,8,'Michelin')

    def aceleration(self, velocity = 'slow'):
        if velocity == 'fast':
            self._motor.gas_inyection(10)
        else:
            self._motor.gas_inyection(3)
        
        self._state = 'moving'
    
    def vehicle_information(self):
        information = f"""
        ---General information---
        Model = {self.model}
        Brand = {self.brand}
        Color = {self.color}
        Year = {self.year}
        
        ---Motor information---
        Cylindres = V{self._motor.cylinders}
        Combustible = {self._motor.combustible}
        Liters = {self._motor.liters}L

        ---Tires information---
        Type = {self.tires.type_of_tire}
        Radius = {self.tires.radius}''
        Width = {self.tires.width}''
        PSI = {self.tires.psi} lb

        
        """
        print(information)

class Motor:

    def __init__(self, cylinders, liters = 3.2 ,combustible = 'gasoline'):
        self.cylinders = cylinders
        self.liters = liters
        self.combustible = combustible
        self._temperature = 0

    def gas_inyection(self, cuantity ):
        pass


class Tires:

    def __init__(self, type_of_tire, radius, width, brand):
        self.type_of_tire = type_of_tire
        self.radius = radius
        self.width = width
        self.brand = brand
        self.psi = 15
    
    def inflate_tires(self, psi_added):
        print("Inflating tires.....")
        os.system("sleep 3")
        self.psi = self.psi + psi_added
        print("\nTires inflated")


if __name__ == "__main__":
    my_first_vehicle = Automobile("Cheyenne","Chevrolet","Black", 2017)
    my_first_vehicle._motor = Motor(8,6.2, "Gasoline")  
    my_first_vehicle.tires = Tires("All terrain", 20, 12, "Goodyear") 
    my_first_vehicle.vehicle_information()
    my_first_vehicle.tires.inflate_tires(35)
    my_first_vehicle.vehicle_information()


        

