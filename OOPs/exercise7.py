class Employee:
    num_employees = 0

    def __init__(self, first_name, last_name, position):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position

        Employee.num_employees += 1

    def get_num_employees(self):
        return self.num_employees
emp1 = Employee('John', 'Smith', 'Developer')
emp2 = Employee('Mary', 'Smith', 'Tester')
print(Employee.num_employees)
