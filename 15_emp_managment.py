class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annualSalary(self):
        return self.monthly_salary * 12
    

emp1 = Employee("Osama", 400000)
emp2 = Employee("Umar", 100000)

print(emp1.annualSalary())
print(emp2.annualSalary())
