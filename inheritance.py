class Person():
      
    # Constructor
    def __init__(self, name):
        self.name = name
  
    # To get name
    def getName(self):
        return self.name
  
    # To check if this person is employee
    def isEmployee(self):
        return False
  
  
# Inherited or Sub class (Note Person in bracket)
class Employee(Person):

    def getName(self):

        return "Hello " + self.name

    def isEmployee(self):
        return True
    pass


# Driver code
per = Person("Geek1")  # An Object of Person
print(per.getName(), per.isEmployee())
  
emp = Employee("Geek2") # An Object of Employee
print(emp.getName(), emp.isEmployee())