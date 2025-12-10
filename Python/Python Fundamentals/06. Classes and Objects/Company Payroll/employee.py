# Create an employee
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self. salary = salary

    # Calculate monthly salary
    def calculate_salary(self):
        return self.salary / 12