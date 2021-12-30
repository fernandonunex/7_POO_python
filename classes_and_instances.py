class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@web.com'        

        Employee.num_of_emps += 1

    def full_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = self.raise_amount * self.pay

#---------------------Instances-----------------------
emp_1 = Employee('Fernando', 'Nunez', 70000)
emp_2 = Employee('Eric', 'Ries', 1000000)

#--------------Calling atributes---------------------
# print(emp_1.pay)
# print(emp_2.email)

#-----------Calling Methods-----------------------
#print(emp_1.full_name())
#print(Employee.full_name(emp_2))

#----------Class variables and instance variables--------
# print(emp_1.num_of_emps)
# print(Employee.num_of_emps)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# emp_1.raise_amount = 1.8
# print(emp_1.raise_amount)
# Employee.num_of_emps = 8
# print(emp_1.num_of_emps)
# print(emp_2.num_of_emps)

print(emp_1.pay)
print(emp_2.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(emp_2.pay)


