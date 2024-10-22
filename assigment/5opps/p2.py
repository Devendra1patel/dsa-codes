# Problem 2: Employee Management Create a class representing an employee with attributes like employee ID,
# name, and salary. Implement methods to calculate the yearly bonus and display employee details.

class EmployeeManagement:
    def __init__(self,id, name, salary):
        self.id = id
        self.name = name
        self.salary = int(salary)
        
    def details(self):
        print(f"{self.id}   {self.name}   {self.salary}")
        
    def bonus(self):
        bon = (self.salary * 12 * 2)/100
        return bon

    
e1 = EmployeeManagement(1, 'Dev', 1000)
e1.details()
tmp = e1.bonus()
print(tmp)