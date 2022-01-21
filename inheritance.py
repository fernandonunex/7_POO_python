class Rectangel:

    def __init__(self, base, height):
        self.base = base
        self.height = height


    def area(self):
        return self.base * self.height
    

class Square(Rectangel):

    def __init__(self, side):
        super().__init__(side, side)

    

if __name__ == '__main__':
    rectang_1 = Rectangel(3,4)
    print(rectang_1.area())

    square_1 = Square(5)
    print(square_1.area())
        