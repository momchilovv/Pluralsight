from employee import Employee

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
            print(f"Employee {index}: {employee.first_name} {employee.last_name}, earning ${employee.salary}/month.")
            index += 1

def main():
    # Create a new company
    my_company = Company("BBC Top Gear")
    
    # Add employees
    employee1 = Employee("Jeremy", "Clarkson", 50000)
    employee2 = Employee("James", "May", 45000)
    employee3 = Employee("Richard", "Hammond", 47500)

    # Hire employees
    my_company.add_employee(employee1)
    my_company.add_employee(employee2)
    my_company.add_employee(employee3)

    print(f"My company - {my_company.company_name} has a total of {len(my_company.employees)} employees:")
    my_company.print_employees()

main()