# Create an employee
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
# Salary Employee inherits from the base Employee class
class SalaryEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self. salary = salary

    # Calculate monthly salary
    def calculate_payment(self):
        return self.salary / 12
    
# Hourly Employee inherits from the base Employee class
class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, weekly_hours, hour_rate):
        super().__init__(first_name, last_name)
        self.weekly_hours = weekly_hours
        self.hour_rate = hour_rate

    # Calculate weekly payment
    def calculate_payment(self):
        return self.weekly_hours * self.hour_rate
    
# Commission Employee inherits from the base Employee class
class CommissionEmployee(Employee):
    def __init__(self, first_name, last_name, deals_made, deals_worth, commission):
        super().__init__(first_name, last_name)
        self.deals_made = deals_made
        self.deals_worth = deals_worth
        self.commission = commission

    # Calculate comission payment
    def calculate_payment(self):
        return self.deals_made * self.deals_worth * (self.commission / 100)