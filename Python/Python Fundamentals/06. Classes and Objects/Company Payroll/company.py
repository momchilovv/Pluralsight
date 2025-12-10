from employee import CommissionEmployee, HourlyEmployee, SalaryEmployee

# Create the company class
class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []
    # Add a list with employees
    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    # Print Employees details
    def print_employees(self):
        index = 1
        for employee in self.employees:
            print(f"Employee {index}: {employee.first_name} {employee.last_name}, earning ${employee.calculate_payment():.2f}.")
            index += 1

def main():
    # Create a new company
    my_company = Company("BBC Top Gear")
    
    # Add employees
    employee1 = SalaryEmployee("Jeremy", "Clarkson", 51337)
    employee2 = HourlyEmployee("James", "May", 40, 37)
    employee3 = CommissionEmployee("Richard", "Hammond", 5, 1560, 5)

    # Hire employees
    my_company.add_employee(employee1)
    my_company.add_employee(employee2)
    my_company.add_employee(employee3)

    print(f"My company - {my_company.company_name} has a total of {len(my_company.employees)} employees:")
    my_company.print_employees()

main()