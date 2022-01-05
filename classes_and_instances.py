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
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        
    def print_emps(self):
        for emp in self.employees:
            print(f"----> {emp.full_name()}")
    


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


# print(emp_1.pay)
# print(emp_2.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# print(emp_2.pay)

#----------Classmethods and staticmethods------------
# Employee.set_raise_amount(1.08)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

#Creating an alternative to constructor of a class
#CLASSMETHOD
# new_emp_3 = Employee.from_string('Juan-Munson-80000')

# print(new_emp_3.email)
# print(new_emp_3.pay)

# #STATICMETHOD
# import datetime
# my_date = datetime.date(2022, 1, 10)

# print(Employee.is_workday(my_date))

#----------------Inheritance - Creating Subclasses-------------

dev_1 = Developer('Vicente', 'Fernandez', 150000, 'Python')
dev_2 = Developer('Junior', 'H', 90000, 'Ruby')

#print(dev_1.email)
# print(help(Developer))  This line print information about something

mgr = Manager('Laptop', 'Hp', 50, [dev_1,dev_2])

# print(mgr.pay)
# mgr.print_emps()

# mgr.add_emp(emp_1)
# print("*****")
# mgr.print_emps()
# mgr.remove_emp(dev_1)
# print("*****")
# mgr.print_emps()

# print(issubclass(Employee, Manager))
