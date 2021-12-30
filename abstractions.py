class Washing_machine:

    def __init__(self):
        pass

    def wash(self, temperature='Caliente'):
        self._fill_water_tank(temperature)
        self._add_soap()
        self._wash()
        self._centrifugate()

    def _fill_water_tank(self, temperature):
        print(f"Filling the water tank with {temperature}")

    def _add_soap(self):
        print("Adding soap")

    def _wash(self):
        print("Washing the clothes")

    def _centrifugate(self):
        print("Centrifugating the clothes")
    

if __name__ == "__main__":
    lav_1 = Washing_machine()
    lav_1.wash()

    