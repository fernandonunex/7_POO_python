class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(f'The max price is {self.__maxprice}')

    def set_maxprice(self, price):
        self.__maxprice =  price

#DEFAULT
print('DEFAULT')
c = Computer()
c.sell()

#TRYING CHANGING THE ATRIBUTE
print('TRYING CHANGING THE ATRIBUTE')
c.__maxprice = 50
c.sell()    

#USING A METHOD
print('DEFAULT')
c.set_maxprice(50)
c.sell()    
