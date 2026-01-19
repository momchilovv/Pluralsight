# In this exercise, we'll create an employee class that's going to be used in company's internal management system to store 
# employees info, like name, salary, department, title, etc.
# This is a mock data, and it tests only editing and displaying the data. It's not connected to working management system.

class Employee:
    def __init__(self, name, age, salary, currency, country, start_date, in_notice_period, months_since_last_promotion, title, department):
        self.name = name # Employee's name
        self.age = age # Employee's age
        self.salary = salary # Employee's salary
        self.currency = currency # In what currency the employee recieves the salary
        self.country = country # Where the employee is based
        self.start_date = start_date # When the employee joined the company
        self.in_notice_period = in_notice_period # Is in a notice period
        self.months_since_last_promotion = months_since_last_promotion # When was his last promotion, start date is used if never
        self.title = title  # Employee's title
        self.department = department # In which team the employee works

# Create a test employee
test_employee = Employee(
    name = "John",
    age = 34,
    salary = 3490,
    currency = "BGN",
    country = "Bulgaria",
    start_date = "10.09.2023",
    in_notice_period = False,
    months_since_last_promotion = 4,
    title = "Sales Manager",
    department = "Sales",
)

# Print test employee's data
print(f"Name: {test_employee.name}, Age: {test_employee.age}, Title: {test_employee.title}, Team: {test_employee.department}")
print(f"Salary: {test_employee.salary}{test_employee.currency}, Country: {test_employee.country}, Start Date: {test_employee.start_date}")

# Change employee's data:
test_employee.title = "Sales Director" # John is promoted to Sales Director
test_employee.salary = 5980 # His salary is increased
test_employee.months_since_last_promotion = 0 # And the months since last promotion is set to 0 as he was just promoted