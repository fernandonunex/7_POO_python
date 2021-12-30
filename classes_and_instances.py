class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@web.com'        

    def full_name(self):
        return f'{self.first} {self.last}'

#Instances
emp_1 = Employee('Fernando', 'Nunez', 70000)
emp_2 = Employee('Eric', 'Ries', 1000000)

#Calling atributes
# print(emp_1.pay)
# print(emp_2.email)

#Calling Methods
print(emp_1.full_name())
print(Employee.full_name(emp_2))


