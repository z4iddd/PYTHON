class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
        
        
        self.hra_percent = 20
        self.da_percent = 10
        self.tax_percent = 5
    def calculate_hra(self):
        return (self.basic_salary*self.hra_percent) / 100

    
    def calculate_da(self):
        return (self.basic_salary*self.da_percent) / 100

    def calculate_tax(self):
        return (self.basic_salary * self.tax_percent) / 100

    def calculate_gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()

    def calculate_net_salary(self):
        return self.calculate_gross_salary() - self.calculate_tax()

    def display_details(self):
        print("---Employee Salary Report---")

        print("Employee ID   :", self.emp_id)
        print("Employee Name :", self.name)
        print("Basic Salary  :", self.basic_salary)
        print("HRA           :", self.calculate_hra())
        print("DA            :", self.calculate_da())
        print("Tax Deduction :", self.calculate_tax())
        print("Gross Salary  :", self.calculate_gross_salary())
        print("Net Salary    :", self.calculate_net_salary())

emp_id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))

emp = Employee(emp_id, name, basic_salary)

emp.display_details()