

class Employee:

    
    def __init__(self, name="", age=0, emp_id="", salary=0):
        self.name = name
        self.age = age
        self.__employee_id = emp_id      
        self.__salary = salary           

    
    def get_employee_id(self):
        return self.__employee_id

    
    def set_employee_id(self, emp_id):
        self.__employee_id = emp_id

    
    def get_salary(self):
        return self.__salary

    
    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        print("\nEmployee Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.__salary)

    
    def __del__(self):
        pass




class Manager(Employee):

    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    
    def display(self):
        super().display()
        print("Department:", self.department)




class Developer(Employee):

    def __init__(self, name, age, emp_id, salary, language):
        super().__init__(name, age, emp_id, salary)
        self.programming_language = language

    
    def display(self):
        super().display()
        print("Programming Language:", self.programming_language)




employee = None
manager = None
developer = None

while True:

    print("\n--- Python OOP Project: Employee Management System ---")
    print("1. Create Employee")
    print("2. Create Manager")
    print("3. Create Developer")
    print("4. Show Details")
    print("5. Check Subclass")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    
    if choice == 1:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))

        employee = Employee(name, age, emp_id, salary)
        print("Employee created successfully.")


    elif choice == 2:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        dept = input("Enter Department: ")

        manager = Manager(name, age, emp_id, salary, dept)
        print("Manager created successfully.")

    
    elif choice == 3:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float