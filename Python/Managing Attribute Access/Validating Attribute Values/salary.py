import logging

MINIMUM_WAGE = 1000.00

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.set_salary(salary)

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

    def get_salary(self):
        logging.info(f"Someone viewed the salary of {self.name}")
        return f"${self.salary:.2f}"
    
    def set_salary(self, salary):
        if salary < MINIMUM_WAGE:
            raise ValueError(f"${salary:.2f} is below the minimum wage! Minimum wage: ${MINIMUM_WAGE:.2f}")
        
        self.salary = salary
