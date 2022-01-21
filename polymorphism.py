class Person:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def move(self):
        print('I am walking')


class Cyclista(Person):

    def __init__(self, nombre):
        super().__init__(nombre)

    def move(self):
        print('I am riding on my bike')


def main():
    person_1 = Person('Fernando')
    person_1.move()

    cyclist_1 = Cyclista('Juan')
    cyclist_1.move()


if __name__ == '__main__':
    main()